from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from ..models import Employee, Shift


@login_required
def employeeList(request):
  ''' 
    View for list of employees
    Allowed verbs: GET
    returns rendered list of all employees for the current user
  '''

  # check that request is a GET
  if request.method == "GET":
    # get our user info and assign it to current_user
    current_user = request.user
    # filter through all of our employees for the logged in manager and assign to all_employees
    all_employees = Employee.objects.filter(manager_id=current_user.id)
    # pass all_employees data to template
    context = { 'all_employees' : all_employees }
    return render(request, 'website/employee_list.html', context)



     