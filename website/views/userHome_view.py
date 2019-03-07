from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


def userHome(request):
    context = {}
    return render(request, 'website/user_home.html', context)