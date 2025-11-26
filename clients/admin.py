from django.contrib import admin
from .models import Client, Testimonial

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'website', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'client', 'rating', 'is_featured', 'is_approved', 'created_at']
    list_filter = ['is_featured', 'is_approved', 'rating', 'created_at']
    list_editable = ['is_featured', 'is_approved']
    search_fields = ['author_name', 'client__name', 'content']