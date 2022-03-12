from django.db import models


class PlatsAndEquipment(models.Model):
    name = models.CharField(max_length=255)
    unit = models.IntegerField()
    company = models.CharField(max_length=255)
    capacity = models.IntegerField()
    age_and_condition = models.CharField(max_length=255)
    present_location = models.CharField(max_length=255)
    ownership = models.CharField(max_length=255)

    def __str__(self):
        return self.name
