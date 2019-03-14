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

class DateInput(forms.DateInput):
  input_type = 'date'

class EmployeeForm(forms.ModelForm):
  
  class Meta:
    model = Employee
    fields = ('first_name', 'last_name', 'pay_rate', 'start_date', 'pin_code',)
    widgets = {
      'start_date': DateInput(),
    }

class EmployeeEditForm(forms.ModelForm):
  
  class Meta:
    model = Employee
    fields = ('first_name', 'last_name', 'pay_rate', 'start_date', 'pin_code', 'end_date',)
    widgets = {
      'start_date': DateInput(),
      'end_date': DateInput(),
    }
    labels = {
      'first_name': 'First Name',
      'last_name': 'Last Name',
      'pay_rate': 'Pay Rate',
      'start_date': 'Start Date',
      'pin_code': 'Pin Code',
      'end_date': 'Make Inactive',
    }

class UserEditForm(forms.ModelForm):

  class Meta:
    model = User
    fields = ('username', 'email', 'first_name', 'last_name',)

class ManagerEditForm(forms.ModelForm):
    
  class Meta:
    model = Manager
    fields = ('company_name', 'address', 'phone_number',)



