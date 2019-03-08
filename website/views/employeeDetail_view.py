from django.shortcuts import render, get_object_or_404
from website.models import Employee

def employeeDetail(request, employee_id):
  employee = get_object_or_404(Employee, pk=employee_id)
  context = { 'employee': employee}
  return render(request, 'website/employee_detail.html', context)



