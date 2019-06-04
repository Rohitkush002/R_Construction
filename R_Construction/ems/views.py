from django.shortcuts import render, get_object_or_404, redirect

from .form import EmployeeForm
from .models import Employee
from django.contrib import messages


def index(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            contact = form.cleaned_data.get('contact')
            email = form.cleaned_data.get('email')
            address = form.cleaned_data.get('address')
            Designation = form.cleaned_data.get('Designation')
            myform = Employee(name=name, contact=contact, email=email, address=address, Designation=Designation)
            myform.save()
        return redirect('empList')
    data = {
        'form': form,
    }
    return render(request, 'form/index.html', data)


def employee_list(request):
    emp = Employee.objects.all()
    data = {
        'emp': emp
    }
    return render(request, 'form/employee.html', data)


def delete_emp(request, id):
    obj = Employee.objects.get(id=id)

    obj.delete()
    return redirect('empList')
    messages.success(request, 'Records Deleted Successfully....')

    return render(request, 'form/employee.html', data)


def update_emp(request, id=None):
    emp = get_object_or_404(Employee, id=id)
    form = EmployeeForm(request.POST or None, instance=emp)
    if form.is_valid():
        emp.save()
        return redirect('empList')
    messages.success(request, 'Records Deleted Successfully....')
    data = {
        'form': form,
        'emp': emp,
    }
    return render(request, 'form/update.html', data)
