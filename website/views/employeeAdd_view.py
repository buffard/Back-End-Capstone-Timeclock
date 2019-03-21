from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User

from website.models import Employee, Manager
from website.forms import EmployeeForm


def addEmployee(request):

  if request.method == 'POST':
    form_data = request.POST
    pinCode = form_data['pin_code']
    pinCodeCheck = Employee.objects.filter(pin_code=pinCode)
    
    if len(pinCodeCheck) == 1:
      messages.success(request, 'Error: Pin code is already taken')
      employee_form = EmployeeForm()
      template_name = 'website/employee_add.html'
      return render(request, template_name, {'employee_form': employee_form})
      
    else:
      employee = Employee(
        first_name = form_data['first_name'],
        last_name = form_data['last_name'],
        pay_rate = form_data['pay_rate'],
        start_date = form_data['start_date'],
        pin_code = form_data['pin_code'],
        manager = request.user.manager
      )
      employee.save()
      return HttpResponseRedirect(reverse('website:user-home'))


  elif request.method == 'GET':
    employee_form = EmployeeForm()
    template_name = 'website/employee_add.html'
    context = {'employee_form': employee_form}
    return render(request, template_name, context)

