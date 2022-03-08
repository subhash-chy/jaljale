from pyexpat import model
from django.db import models


class Page (models.Model):
    slug = models.CharField(max_length=100)
    title = models.CharField(max_length= 200)
    sub_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title
