from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from ..models import Employee



def userHome(request):
    all_employees = Employee.objects.all()
    context = {'all_employees': all_employees}
    return render(request, 'website/user_home.html', context)