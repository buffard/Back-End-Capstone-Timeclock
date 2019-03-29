from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone 
from website.models import Employee, Shift
import datetime


def clockin(request):

  if request.method == 'POST':
    form_data = request.POST.get('pin_code')
    employee = Employee.objects.get(pin_code=form_data)
    # Filter through the shifts and find the ones where the employee ids match
    # then filter through those to only find shift that have a clock out date equal to null
    shifts = Shift.objects.filter(employee=employee).filter(clock_out_date=None)
    # if there is something within the shifts variable
    if len(shifts) == 1:
      # then select the first shift in the list
      shift = shifts[0]
      # and save a clock out data to that shift
      shift.clock_out_time = timezone.now()
      shift.clock_out_time = shift.clock_out_time.replace(microsecond=0)
      shift.clock_out_date = datetime.date.today()      
      shift.save()
      messages.success(request, 'Clocked Out', extra_tags='alert-danger')

    # if all shifts already have clock out data
    else:
      # then create a new shift and save clock in data
      shift = Shift(
        clock_in_time = timezone.now().replace(microsecond=0),
        clock_in_date = datetime.date.today(),
        employee = employee,      
      )
      shift.save()
      messages.success(request, 'Clocked In', extra_tags='alert-success')
    return HttpResponseRedirect(reverse('website:index'))

  elif request.method == 'GET':
    template_name = 'website/number_pad.html'
    
    return render(request, template_name)


