from django.db import models


class Project (models.Model):
    Ongoing = "Ongoing"
    Completed = "Completed"

    CHOICES = (
        (Ongoing, 'Ongoing'),
        (Completed, 'Completed'),
    )

    name = models.CharField(max_length=255)
    description= models.TextField(blank=True)
    image = models.ImageField(upload_to='project/')
    contract_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    contract_start = models.DateField(blank=True, null=True)
    contract_end = models.DateField(blank=True, null=True)
    employee_name = models.CharField(max_length=255, blank=True, null=True)
    employee_address = models.CharField(max_length=255, blank=True, null=True)
    project_location = models.CharField(max_length=255, blank=True, null=True)

    status = models.CharField(max_length=255, choices=CHOICES, default=Ongoing)


    def __str__(self):
        return self.name
