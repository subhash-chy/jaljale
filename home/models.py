from django.db import models


class Banner(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='banner/')

    def __str__(self):
        return self.title



