from django.contrib.auth.models import User
from django.db import models


class Manager(models.Model):
    company_name = models.CharField(max_length=35)
    address = models.CharField(max_field=75)
    phone_number = models.IntegerField()

class Employee(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    pay_rate = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    pin_code = models.IntegerField()
    manager_id = models.ForeignKey("Manager", on_delete=models.CASCADE)


