from django.urls import path


from .views import employee_view, employee_add
urlpatterns = [
    path('', employee_view,name= 'employee_view'),
    path('employee/add', employee_add ,name= 'employee_add')
]