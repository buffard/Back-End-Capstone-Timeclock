from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from ..models import Employee


def inactiveEmployee(request):
    """ returns a lists of all employees in the Employees table """
    all_employees = Employee.objects.all()
    context = { 'all_employees' : all_employees }
    return render(request, 'website/inactiveEmployee_list.html', context)