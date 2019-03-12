from django.contrib.auth.models import User
from django.db import models



class Manager(models.Model):
  user = models.OneToOneField(User, on_delete=models.PROTECT)
  company_name = models.CharField(max_length=35)
  address = models.CharField(max_length=75)
  phone_number = models.IntegerField()
    

class Employee(models.Model):
  first_name = models.CharField(max_length=12)
  last_name = models.CharField(max_length=12)
  pay_rate = models.IntegerField()
  start_date = models.DateField(default=None, null=True)
  end_date = models.DateField(default=None, null=True, blank=True)
  pin_code = models.IntegerField()
  deactivate = models.BooleanField(default=False)
  manager = models.ForeignKey("Manager", on_delete=models.CASCADE)

class Shift(models.Model):
  clock_in_time = models.TimeField(default = None, null=True)
  clock_out_time = models.TimeField(default = None, null=True)
  clock_in_date = models.DateField(default = None, null=True)
  clock_out_date = models.DateField(default = None, null=True)
  employee = models.ForeignKey("Employee", on_delete=models.CASCADE)
