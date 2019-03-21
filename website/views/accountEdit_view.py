from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from website.models import User, Manager
from website.forms import UserEditForm, ManagerEditForm


def accountEdit(request, manager_id):
  '''
    View for account edit. This view allows users to edit their account information. 
    
    Allowed verbs: GET, POST
    
    returns a form to edit the user's account and then posts to database
    '''

  # get our current user's information
  user = get_object_or_404(User, pk=manager_id)
  # get our current user's' manager information
  manager = get_object_or_404(Manager, pk=manager_id)
  # check to see if our request is for a POST
  if request.method == 'POST':
    
    form_data = request.POST
  
    user.username = form_data['username']
    user.email = form_data['email']
    user.first_name = form_data['first_name']
    user.last_name = form_data['last_name']
    manager.company_name = form_data['company_name']
    manager.address = form_data['address']
    manager.phone_number = form_data['phone_number']
   

    user.save()
    manager.save()
    return HttpResponseRedirect(reverse('website:account', args=[user.id]))
  
  elif request.method == 'GET':
    user_form = UserEditForm(instance= user)
    manager_form = ManagerEditForm(instance= manager)
    template_name = 'website/account_edit.html'
    context = {'user_form': user_form, 'manager_form': manager_form}
    return render(request, template_name, context)




