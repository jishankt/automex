from django.contrib import admin
from .models import Project, ProjectStat

class ProjectStatInline(admin.TabularInline):
    model = ProjectStat
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'client', 'category', 'start_date', 'is_featured', 'is_published']
    list_filter = ['category', 'is_featured', 'is_published', 'start_date']
    list_editable = ['is_featured', 'is_published']
    search_fields = ['title', 'client', 'short_description']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectStatInline]

@admin.register(ProjectStat)
class ProjectStatAdmin(admin.ModelAdmin):
    list_display = ['project', 'title', 'value']
    list_filter = ['project']
    search_fields = ['title', 'project__title']