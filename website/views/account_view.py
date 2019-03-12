from django.shortcuts import render, get_object_or_404
from website.models import User, Manager

def account(request, manager_id):
  user = get_object_or_404(User, pk=manager_id)
  manager = get_object_or_404(Manager, pk=manager_id)

  context = { 'user': user, 'manager': manager}
  return render(request, 'website/account_detail.html', context)

  

