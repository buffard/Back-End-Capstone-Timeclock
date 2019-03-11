from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from ..models import Shift


def shiftList(request):
    """ returns a lists of all shifts in the Shift table """
    all_shifts = Shift.objects.all()
    context = { 'all_shifts' : all_shifts }
    return render(request, 'website/employee_detail.html', context)