from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from .models import Employee, Department

# Create your views here.
from .forms import EmployeeForm


def employee_view(request):

    employee = get_list_or_404(Employee)

    return render(request, "home.html", context={"employee": employee})


# def employee_add(request):
#     departments = Department.objects.all()
#     employees = Employee.objects.all()

#     if request.method == 'POST':
#         Employee.objects.create(
#             first_name=request.POST.get('first_name'),
#             last_name=request.POST.get('last_name'),
#             email=request.POST.get('email'),
#             address=request.POST.get('address'),
#             image=request.FILES.get('image') or None,
#             department_id=request.POST.get('department'),
#             manager_id=request.POST.get('manager') or None,
#         )

#         return redirect('employee_view')

#     return render(request, 'employee_add.html', {
#         'departments': departments,
#         'employees': employees,
#     })


def employee_add(request):

    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("employee_view")
        else:
            print(form.errors)
    else:
        print(request.method)
    form = EmployeeForm()
    return render(request, "employee_add.html", {"form": form})


def employee_detail(request, id):
    employee = Employee.objects.get(id=id)

    context = {"employee": employee}

    return render(request, "employee_detail.html", context)


def employee_edit(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES, instance=employee)

        if form.is_valid():
            form.save()
            return redirect("employee_view")
        else:
            print(form.errors)
    else:
        form = EmployeeForm(instance=employee)

    context = {"employee": employee, "form": form}

    return render(request, "employee_edit.html", context=context)


def employee_delete(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        employee.delete()
        redirect("employee_view")

    return redirect("employee_view")
