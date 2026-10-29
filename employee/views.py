from django.shortcuts import render, get_list_or_404 , redirect
from .models import Employee, Department
# Create your views here.
from django.http import HttpResponse

def employee_view(request):

    employee = get_list_or_404(Employee)
     
    return render(request, 'home.html', context= {'employee': employee})

def employee_add(request):
    departments = Department.objects.all()
    employees = Employee.objects.all()

    if request.method == 'POST':
        Employee.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            image=request.FILES.get('image') or None,
            department_id=request.POST.get('department'),
            manager_id=request.POST.get('manager') or None,
        )

        return redirect('employee_view')

    return render(request, 'employee_add.html', {
        'departments': departments,
        'employees': employees,
    })