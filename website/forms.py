from django.contrib.auth.models import User
from django import forms
from website.models import Manager, Employee


class UserForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput())

  class Meta:
      model = User
      fields = ('username', 'email', 'password', 'first_name', 'last_name',)

class ManagerForm(forms.ModelForm):
    
  class Meta:
    model = Manager
    fields = ('company_name', 'address', 'phone_number',)

class EmployeeForm(forms.ModelForm):
  
  class Meta:
    model = Employee
    fields = ('first_name', 'last_name', 'pay_rate', 'start_date', 'pin_code',)
  



