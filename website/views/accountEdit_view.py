from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from website.models import User, Manager
from website.forms import UserEditForm, ManagerEditForm


def accountEdit(request, manager_id):
  user = get_object_or_404(User, pk=manager_id)
  manager = get_object_or_404(Manager, pk=manager_id)
  
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
    return HttpResponseRedirect(reverse('website:account'))
  
  elif request.method == 'GET':
    user_form = UserEditForm(instance= user)
    manager_form = ManagerEditForm(instance= manager)
    template_name = 'website/account_edit.html'
    context = {'user_form': user_form, 'manager_form': manager_form}
    return render(request, template_name, context)




