from django.db import models

class Service(models.Model):
    CHOICES = (
        (1, 1),
        (2, 2),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    column = models.IntegerField(choices=CHOICES, default=1)


    def __str__(self):
        return self.title
