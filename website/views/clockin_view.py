from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.utils import timezone 
import datetime

from website.models import Employee, Shift



def clockin(request):

  if request.method == 'POST':
    form_data = request.POST.get('pin_code')
    employee = Employee.objects.get(pin_code=form_data)
    shifts = Shift.objects.filter(employee=employee).filter(clock_out_date=None)
    print("AAAAAAAAAAAAAAAA", employee)
    print("BBBBBBBBBB", shifts)
    
    if len(shifts) == 1:
      shift = shifts[0]
      print("CCCCCCCCCCCCC", shift)
      
      shift.clock_out_time = timezone.now()
      shift.clock_out_date = datetime.date.today()      
      shift.save()

    else:
      shift = Shift(
        clock_in_time = timezone.now(),
        clock_in_date = datetime.date.today(),
        employee = employee,      
      )
      shift.save()

    return HttpResponseRedirect(reverse('website:index'))

  elif request.method == 'GET':
    
    template_name = 'website/number_pad.html'
    
    return render(request, template_name)