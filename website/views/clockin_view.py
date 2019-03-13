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
    print("HEHEHEHEHEHEHEHEHEHEH", employee)
    # TODO:if statement
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