from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.exceptions import FieldError
from .models import Post, Category

def post_list(request):
    try:
        posts = Post.objects.filter(is_published=True).order_by('-created_at')
        
        # Search functionality
        query = request.GET.get('q')
        if query:
            posts = posts.filter(
                Q(title__icontains=query) |
                Q(excerpt__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct()
        
        # Category filter
        category_slug = request.GET.get('category')
        if category_slug:
            posts = posts.filter(category__slug=category_slug)
        
        featured_posts = posts.filter(is_featured=True)[:3]
        categories = Category.objects.all()
        
    except FieldError as e:
        # Handle database schema issues
        posts = Post.objects.none()
        featured_posts = Post.objects.none()
        categories = Category.objects.none()
        print(f"Database error: {e}")  # For debugging
    
    context = {
        'posts': posts,
        'featured_posts': featured_posts,
        'categories': categories,
        'query': query,
        'selected_category': category_slug,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    related_posts = Post.objects.filter(is_published=True, category=post.category).exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'related_posts': related_posts,
    }
    return render(request, 'blog/post_detail.html', context)

def category_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'blog/categories.html', context)