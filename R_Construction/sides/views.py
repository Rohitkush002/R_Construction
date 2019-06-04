from django.shortcuts import render, get_object_or_404, redirect
from .forms import SideForm, SideInchargeForm, WorkForm
from django.contrib import messages
from .models import Side, Work


def side(request):
    form = SideForm()
    if request.method == 'POST':
        form = SideForm(request.POST or None)
        if form.is_valid():
            sideName = form.cleaned_data.get('sideName')
            sideAdd = form.cleaned_data.get('sideAdd')
            sideIncharge = form.cleaned_data.get('sideIncharge')
            vehicles = form.cleaned_data.get('vehicles')
            employee = form.cleaned_data.get('employee')
            activeVehicle = form.cleaned_data.get('activeVehicle')
            myform = Side(sideName=sideName, sideAdd=sideAdd, sideIncharge=sideIncharge, vehicles=vehicles,
                          employee=employee, activeVehicle=activeVehicle)
            myform.save()
        return redirect('sideList')
    data = {
        'form': form,
    }
    return render(request, 'sides.html', data)


def sidelist(request):
    sd = Side.objects.all()
    data = {
        'sd': sd
    }
    return render(request, 'sideList.html', data)


def work(request):
    form = WorkForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('workList')

    data = {
        'form': form
    }
    return render(request, 'work.html', data)


def workList(request):
    wl = Work.objects.all()
    data = {
        'wl': wl
    }
    return render(request, 'worklist.html', data)


def delete(request, id):
    obj = Side.objects.get(id=id)

    obj.delete()
    return redirect('sideList')
    messages.success(request, 'Records Deleted Successfully....')

    return render(request, 'sideList.html', data)


def deleteWork(request, id):
    obj = Work.objects.get(id=id)
    obj.delete()
    return redirect('workList')
    messages.success(request, 'Records Deleted Successfully....')

    return render(request, 'workList.html', data)


def update(request, id=None):
    sd = get_object_or_404(Side, id=id)
    form = SideForm(request.POST or None, instance=sd)
    if form.is_valid():
        sd.save()
        return redirect('sideList')
    messages.success(request, 'Records Updated Successfully....')
    data = {
        'form': form,
        'sd': sd,
    }
    return render(request, 'update.html', data)


def sideincharge(request):
    form = SideInchargeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('side')
    data = {
        'form': form
    }
    return render(request, 'sideIncharge.html', data)


def workingSide(request, id):
    site = Side.objects.get(sideName=id)

    d = {
        'sidelist': site
    }
    return render(request, 'workingSide.html', d)
