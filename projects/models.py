from django.db import models
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

class Project(models.Model):
    PROJECT_CATEGORIES = [
        ('web_development', 'Web Development'),
        ('mobile_app', 'Mobile App'),
        ('digital_marketing', 'Digital Marketing'),
        ('business_automation', 'Business Automation'),
        ('consulting', 'Business Consulting'),
        ('data_analytics', 'Data Analytics'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    client = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=PROJECT_CATEGORIES)
    short_description = models.TextField()
    description = RichTextField()
    challenge = RichTextField(blank=True)
    solution = RichTextField(blank=True)
    results = RichTextField(blank=True)
    
    # Project Details
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    project_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    
    # Images
    main_image = models.ImageField(upload_to='projects/')
    image_1 = models.ImageField(upload_to='projects/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='projects/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='projects/', blank=True, null=True)
    
    # Status
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    
    # SEO
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    
    tags = TaggableManager(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.title} - {self.client}"

class ProjectStat(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='stats')
    title = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
    icon = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return f"{self.project.title} - {self.title}"