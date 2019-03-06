from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


def loginRegistration(request):
    return render(request, 'website/login_registration.html')