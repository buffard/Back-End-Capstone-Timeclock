from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404

from website.models import Shift

def clockinDelete(request, shift_id):
    
    shift = get_object_or_404(Shift, pk=shift_id)

    shift.delete()
    return HttpResponseRedirect(reverse('website:employeeDetail', args=[shift.employee.id]))
