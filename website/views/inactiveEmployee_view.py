from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from ..models import Employee


@login_required
def inactiveEmployee(request):
  """ returns a lists of all inactive employees to the inactive employees table """
  if request.method == "GET":
    current_user = request.user
    all_employees = Employee.objects.filter(manager_id=current_user.id)
    context = { 'all_employees' : all_employees }
    return render(request, 'website/inactiveEmployee_list.html', context)