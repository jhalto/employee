from django.urls import path


from .views import employee_view, employee_add, employee_detail, employee_edit, employee_delete
urlpatterns = [
    path('', employee_view,name= 'employee_view'),
    path('employee/add', employee_add ,name= 'employee_add'),
    path('employee/detail/<int:id>', employee_detail ,name= 'employee_detail'),
    path('employee/edit/<int:id>', employee_edit ,name= 'employee_edit'),
    path('employee/delete/<int:id>', employee_delete ,name= 'employee_delete')
]