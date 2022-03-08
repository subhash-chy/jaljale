from django.db import models


class SiteSetting (models.Model):
    logo = models.ImageField(upload_to='logo/')
    facebook_url = models.CharField(max_length=100)
    twitter_url = models.CharField(max_length=100)
    instagram_url = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    company_brief = models.TextField()
    google_map= models.TextField(null=True, blank=True)

    def __str__(self):
        return self.email
