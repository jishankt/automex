from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='clients/')
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name

class Testimonial(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='testimonials')
    author_name = models.CharField(max_length=100)
    author_position = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    is_featured = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Testimonial by {self.author_name} from {self.client.name}"