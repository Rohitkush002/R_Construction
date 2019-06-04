from django.urls import path
from . import views as emp_view

urlpatterns = [
    path('index', emp_view.index, name='home'),
    path('emplist', emp_view.employee_list, name='empList'),
    path('update/<int:id>', emp_view.update_emp, name='update-emp'),
    path('delete/<int:id>', emp_view.delete_emp, name='delete-emp'),

]
