from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from website.models import Shift
from website.forms import ShiftEditForm


def clockinEdit(request, shift_id):
  shift = get_object_or_404(Shift, pk=shift_id)
  
  if request.method == 'POST':
    form_data = request.POST
    shift.clock_in_time = form_data['clock_in_time']
    shift.clock_in_date = form_data['clock_in_date']
    shift.clock_out_time = form_data['clock_out_time']
    shift.clock_out_date = form_data['clock_out_date']

    shift.save()
    return HttpResponseRedirect(reverse('website:employeeDetail', args=[shift.employee.id]))
  
  if request.method == 'GET':
    shift_form = ShiftEditForm(instance=shift)
    template_name = 'website/clockin_edit.html'
    context = {'shift_form': shift_form, 'shift': shift_id, 'employee': shift.employee.id}
    return render(request, template_name, context)
