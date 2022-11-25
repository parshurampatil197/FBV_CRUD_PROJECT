from django.shortcuts import render
from .forms import StudentRegForm
from .models import User
from django.http import HttpResponseRedirect


# This function will add new items and show all items
def add_show(request):
    fm = StudentRegForm(request.POST or None)
    if request.method == 'POST' and fm.is_valid():
        fm.save()
        # nm = fm.cleaned_data['name']
        # mail = fm.cleaned_data['email']
        # pwd = fm.cleaned_data['password']
        # user = User(name=nm, email=mail, password=pwd)
        # user.save()
        fm = StudentRegForm()

    stu = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stu})


# This function will edit/Update
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegForm(instance=pi)

    return render(request, 'enroll/updatestu.html', {'form': fm})


# This Function will delete
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
