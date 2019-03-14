from django.conf.urls import url
from django.urls import path

from website import views

app_name = "website"
urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^login$', views.login_user, name='login'),
  url(r'^logout$', views.user_logout, name='logout'),
  url(r'^register$', views.register, name='register'),
  path('loginRegistration/', views.loginRegistration, name='loginRegistration'),
  path('user-home/', views.userHome, name='user-home'),
  path('employees/', views.employeeList, name='employeeList'),
  path('employees/<int:employee_id>/', views.employeeDetail, name='employeeDetail'),
  path('addemployee/', views.addEmployee, name='addEmployee'),
  path('editemployee/<int:employee_id>/', views.editEmployee, name='editEmployee'),
  path('inactiveEmployee/', views.inactiveEmployee, name='inactiveEmployee'),
  path('account/<int:manager_id>/', views.account, name='account'),
  path('accountEdit/<int:manager_id>/', views.accountEdit, name='accountEdit'),
  path('clockin/', views.clockin, name='clockin'),
  path('clockin/edit/<int:shift_id>/', views.clockinEdit, name='clockinEdit'),
]