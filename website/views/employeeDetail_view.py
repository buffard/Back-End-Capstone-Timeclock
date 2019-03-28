from django.shortcuts import render, get_object_or_404
from website.models import Employee, Shift
from datetime import datetime, time, date



def employeeDetail(request, employee_id):
  employee = get_object_or_404(Employee, pk=employee_id)
  all_shifts = Shift.objects.filter(employee_id=employee_id)
  for shift in all_shifts:

    strtime1 = str(shift.clock_in_time)
    strtime2 = str(shift.clock_out_time)
    time1 = datetime.strptime(strtime1, "%H:%M:%S.%f")
    time2 = datetime.strptime(strtime2, "%H:%M:%S.%f")
    #find the difference between two dates
    diff = time2 - time1   
    seconds = diff.seconds
    # shows clock in time
    print("TIME1", time1)
    # shows clock out time
    print("TIME2", time2)
    # shows the difference between times in time format
    print("DIFF", diff)
    # shows seconds between shifts
    print ("Seconds", str(seconds) + ' second(s)')

    
    diff_btw_two_times = (seconds) / 3600
    overall_hours = diff_btw_two_times
    print (str(overall_hours) + ' hours')
    


 




  context = { 'employee': employee, 'all_shifts': all_shifts}
  return render(request, 'website/employee_detail.html', context)







 