from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):
    title = models.CharField(max_length=100)
    profile_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f"About: {self.title} last updated: {self.updated_on}"

