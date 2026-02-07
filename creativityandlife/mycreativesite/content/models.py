from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Video(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='videos')
    video_url = models.URLField(help_text="YouTube or video URL")
    description = models.TextField(blank=True)
    thumbnail = models.URLField(blank=True, help_text="Thumbnail image URL")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class OnlineClass(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    duration = models.CharField(max_length=100, help_text="e.g., 4 weeks, 10 hours")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    interested_class = models.ForeignKey(OnlineClass, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.email}"
    
    class Meta:
        verbose_name_plural = "Enquiries"