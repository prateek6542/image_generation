# imagegen/models.py

from django.db import models

class GeneratedImage(models.Model):
    prompt = models.CharField(max_length=255)
    image_url = models.URLField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.prompt} - {self.image_url}"
