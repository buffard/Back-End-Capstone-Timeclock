from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from ..models import Employee, Shift


@login_required
def userHome(request):
  if request.method == "GET":
    current_user = request.user
    all_employees = Employee.objects.filter(manager_id=current_user.id)
    context = {'all_employees': all_employees}
    return render(request, 'website/user_home.html', context)