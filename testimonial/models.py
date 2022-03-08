from django.db import models


class Testimonial (models.Model):
    name = models.CharField(max_length=100)
    comment= models.TextField()
    image = models.ImageField(upload_to='testimonial/')

    def __str__(self):
        return self.name
