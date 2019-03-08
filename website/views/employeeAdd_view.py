from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponseRedirect


from website.forms import EmployeeForm


def addEmployee(request):

  if request.method == 'POST':
    employee_form = EmployeeForm(data=request.POST)

    if employee_form.is_valid():
      # Save the user's form data to the database.
      employee = employee_form.save()
      employee.save()

      return HttpResponseRedirect(reverse('website:employeeList'))


  elif request.method == 'GET':
    employee_form = EmployeeForm()
    template_name = 'website/employee_add.html'
    return render(request, template_name, {'employee_form': employee_form})