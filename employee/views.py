from django.shortcuts import render, get_list_or_404
from .models import Employee, Department
# Create your views here.
from django.http import HttpResponse

def employee_view(request):

    employee = get_list_or_404(Employee)
     
    return render(request, 'home.html', context= {'employee': employee})

def employee_add(request):

    

    return HttpResponse("asdjfl")