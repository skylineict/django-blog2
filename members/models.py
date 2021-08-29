from django.db import models
from django.db.models.base import Model

purpose_info = [('Sales', "Sales"), ("Traning", "Traning"),
                ('Job', "Job"), ("General Inquries", "General Inquries")

                ]
# Create your models here.


class Contactus(models.Model):
    full_name = models.CharField(max_length=40)
    phone = models.IntegerField()
    purpose = models.CharField(
        max_length=100, choices=purpose_info, default='select')
    email = models.EmailField(max_length=50, default="example@gmail.com")
    comment = models.TextField(max_length=700)
    contact_by = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    def object(self):
        return models.OrderBy('-contact_by')
