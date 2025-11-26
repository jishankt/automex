from django.contrib import admin
from .models import Service, ServiceFeature

class ServiceFeatureInline(admin.TabularInline):
    model = ServiceFeature
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_featured', 'is_active', 'created_at']
    list_editable = ['order', 'is_featured', 'is_active']
    list_filter = ['is_featured', 'is_active', 'created_at']
    search_fields = ['title', 'short_description']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ServiceFeatureInline]

@admin.register(ServiceFeature)
class ServiceFeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'service', 'icon']
    list_filter = ['service']
    search_fields = ['title', 'service__title']