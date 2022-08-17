from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.http import HttpResponse
from . import views
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django import forms

# Create your views here.

def employee_list(request):
    context = {'employee_list': Employee.objects.all()} 
    return render(request, "employee_register/employee_list.html",context)  

def employee_form(request,id=0):
    if request.method == "GET":
        if id==0: 
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)  
        return render(request, "employee_register/employee_form.html",{'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee) 
        if form.is_valid():
            form.save()
        return redirect('/list')

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/list')



#login -------------------
def home(request):
    return render(request, "employee_register/index.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request, "Email already exist! Please try some other email")
            return redirect('home')

        if len(username)>10:
            messages.error(request, "Username too long! Please try some other username")
        
        if pass1 != pass2:
            messages.error(request, "password did not match! Please try some other password")

        if not username.isalnum():
            messages.error(request, "Username must be alpha-numeric")
            return redirect('home')

        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        messages.success(request, 'User created successfully')
        return redirect('signin')
    return render(request, "employee_register/signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            context = {'employee_list': Employee.objects.all()} 
            fname = user.first_name
            return render(request, "employee_register/employee_list.html", context) 
        
        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')

    return render(request, "employee_register/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Succesfully")
    return redirect('home')