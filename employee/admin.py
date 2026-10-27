from django.contrib import admin
from .models import Employee, Department
# Register your models here.
@admin.register(Employee)
class EmployeeModel(admin.ModelAdmin):
    pass

@admin.register(Department)
class DepartmentModel(admin.ModelAdmin):
    pass