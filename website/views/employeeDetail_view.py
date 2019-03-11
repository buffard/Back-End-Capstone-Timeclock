from django.shortcuts import render, get_object_or_404
from website.models import Employee, Shift

def employeeDetail(request, employee_id):
  employee = get_object_or_404(Employee, pk=employee_id)
  all_shifts = Shift.objects.filter(employee_id=employee_id)

  context = { 'employee': employee, 'all_shifts': all_shifts}
  return render(request, 'website/employee_detail.html', context)

  





 