from django.shortcuts import render, get_object_or_404
from website.models import User, Manager

def account(request, manager_id):
  ''' 
    View for Account information

    Allowed verbs: GET

    returns details about the current user's account information
  '''
  
  # get our current user's information
  user = get_object_or_404(User, pk=manager_id)
  # get our current user's' manager information
  manager = get_object_or_404(Manager, pk=manager_id)
  # pass user and manager data to template
  context = { 'user': user, 'manager': manager}
  return render(request, 'website/account_detail.html', context)

  

