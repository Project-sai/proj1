from django.urls import path
from Employee_details import views


urlpatterns = [
    path('emp_list/',views.emp_list,name="employee_list"),
    path('emp_details/<str:empid>/',views.emp_details,name="employee_details"),
    path('emp_update/<str:empid>/',views.emp_update,name="employee_update"),
    path('emp_delete/<str:empid>/',views.emp_delete,name="employee_delete"),
    path('employee_registration/',views.employee_registration,name="employee_registration"),
]