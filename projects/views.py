from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    projects = Project.objects.filter(is_published=True).order_by('-start_date')
    categories = Project.PROJECT_CATEGORIES
    
    # Filter by category
    category = request.GET.get('category')
    if category:
        projects = projects.filter(category=category)
    
    featured_projects = projects.filter(is_featured=True)[:3]
    
    context = {
        'projects': projects,
        'featured_projects': featured_projects,
        'categories': categories,
        'selected_category': category,
    }
    return render(request, 'projects/project_list.html', context)

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug, is_published=True)
    related_projects = Project.objects.filter(is_published=True, category=project.category).exclude(id=project.id)[:3]
    
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'projects/project_detail.html', context)