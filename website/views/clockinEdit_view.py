from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from website.models import Shift
from website.forms import ShiftEditForm


def clockinEdit(request, shift_id):
  shift = get_object_or_404(Shift, pk=shift_id)
  
  print("HERHERHEJKHRJKEHJKR", shift)
  
  # if request.method == 'POST':
  #   form_data = request.POST
  
  #   employee.first_name = form_data['first_name']
  #   employee.last_name = form_data['last_name']
  #   employee.pay_rate = form_data['pay_rate']
  #   employee.start_date = form_data['start_date']
  #   employee.pin_code = form_data['pin_code']
  #   if form_data['end_date'] == '':
  #     employee.end_date = None
  #   else:
  #     employee.end_date = form_data['end_date']

  #   employee.manager = request.user.manager

  #   employee.save()
  #   return HttpResponseRedirect(reverse('website:employeeDetail', args=[employee.id]))
  
  if request.method == 'GET':
    shift_form = ShiftEditForm(instance=shift)
    template_name = 'website/clockin_edit.html'
    context = {'shift_form': shift_form, 'shift': shift_id, 'employee': shift.employee.id}
    print("Cccccccccccccccc", context)
    return render(request, template_name, context)
