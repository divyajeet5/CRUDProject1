from django.shortcuts import render, redirect
from .forms import StudentRegistration
from .models import User
from django.contrib import messages
# Create your views here.

def add_show(request):

    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            if User.objects.filter(email=em):
                messages.error(request, "E-mail already exists, please try another e-mail")
                return redirect('/')
            else:
              pw = fm.cleaned_data['password']
              reg = User(name=nm, email=em, password=pw)
              reg.save()
              fm = StudentRegistration()
    else:
        fm = StudentRegistration()

    student = User.objects.all()
    return render(request, 'enroll/add&show.html', {'foo': fm, 'stud': student})




def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
            pi = User.objects.get(pk=id)
            fm = StudentRegistration(instance=pi)

    return render(request, 'enroll/update.html', {'form': fm})




def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return redirect('/')











