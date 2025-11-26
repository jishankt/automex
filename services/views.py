from django.shortcuts import render, get_object_or_404
from .models import Service

def service_list(request):
    services = Service.objects.filter(is_active=True).order_by('order')
    featured_services = services.filter(is_featured=True)
    
    context = {
        'services': services,
        'featured_services': featured_services,
    }
    return render(request, 'services/service_list.html', context)

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug, is_active=True)
    related_services = Service.objects.filter(is_active=True).exclude(id=service.id)[:3]
    
    context = {
        'service': service,
        'related_services': related_services,
    }
    return render(request, 'services/service_detail.html', context)