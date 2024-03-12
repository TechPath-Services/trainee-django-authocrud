from django.shortcuts import render,redirect
from apps.models import Employees

# Create your views here.

def login_view(request):
    return render(request, 'main/login.html')

def signup_view(request):
    return render(request, 'main/signup.html')

def Index(request):
    return render(request, 'web/index.html')


def Index(request):
    emp = Employees.objects.all()
    context = {
        "emp": emp
    }
    return render(request, 'web/index.html',context)

def Add_Employee(request):
    if  request.method == 'POST':
        name =  request.POST.get('emp_name')
        email = request.POST.get('emp_email') 
        phone = request.POST.get('emp_phone')    
        address = request.POST.get('emp_address')
    
        emp = Employees(
            name= name,
            email= email,
            phone = phone,
            address= address   
        )
        emp.save()
        redirect('home')
    return render(request, 'web/index.html')

def edit_Employee(request):
    if  request.method == 'POST':
        name =  request.POST.get('emp_name')
        email = request.POST.get('emp_email') 
        phone = request.POST.get('emp_phone')    
        address = request.POST.get('emp_address')
    
        emp = Employees(
            name= name,
            email= email,
            phone = phone,
            address= address   
        )
        emp.save()
        redirect('home')
    return render(request, 'web/index.html')