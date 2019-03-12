from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from website.models import Employee, Manager
from website.forms import EmployeeEditForm


def editEmployee(request, employee_id):
  employee = get_object_or_404(Employee, pk=employee_id)
  print('HEREHERE', employee_id)
  if request.method == 'POST':
    form_data = request.POST
  
    employee.first_name = form_data['first_name']
    employee.last_name = form_data['last_name']
    employee.pay_rate = form_data['pay_rate']
    employee.start_date = form_data['start_date']
    employee.pin_code = form_data['pin_code']
    employee.manager = request.user.manager

    employee.save()
    return HttpResponseRedirect(reverse('website:user-home'))
  
  elif request.method == 'GET':
    employee_form = EmployeeEditForm(instance= employee)
    template_name = 'website/employee_edit.html'
    context = {'employeeEdit_form': employee_form, 'employee': employee_id}
    return render(request, template_name, context)

