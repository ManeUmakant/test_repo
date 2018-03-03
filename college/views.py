from django.shortcuts import render, redirect,HttpResponse
from django.http import JsonResponse
from datetime import datetime
from college.forms import MyForm, EmpForm, StudentForm,CreateUserForm,LoginForm,EmployeeForm,ProfileForn,ChangePasword
from college.models import Employee, Student,Employee1,User as db_user, Profile
from django.contrib.auth import login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import logging
import xlsxwriter
from io import StringIO
logger = logging.getLogger(__name__)
from django.conf import settings
#from django.contrib.auth import


def getData(request):
    print(settings.BASE_DIR)
    return HttpResponse("hello")

@login_required(login_url='/college/login')
def changePassword(request):
    form = ChangePasword()
    if request.method == 'POST':
        form = ChangePasword(request.POST)
        if form.is_valid():
            if form.cleaned_data['new_password']  == form.cleaned_data['repeat_password']:
                user = authenticate(username=request.user.username, password=form.cleaned_data['old_password'])
                if user is not None:
                    user = User.objects.get(email=request.user.email)
                    user.set_password(form.cleaned_data['new_password'])
                    user.save()
                    return render(request, 'sites/change_password.html', {'error':'Succcess', 'form':form})
                return render(request, 'sites/change_password.html', {'error': 'Incorrect old password', 'form': form})
            return render(request, 'sites/change_password.html', {'error': 'Password one and Repeat password must match old password', 'form': form})
        return render(request, 'sites/change_password.html', {'error': '', 'form': form})
    return render(request, 'sites/change_password.html', {'error':'','form':form})

def downloadAsExcel(request):

    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Report.xlsx'
    header = 'Sno\t'
    header += 'Name\t'
    header += 'Email\t'
    header += 'Address\t'
    header += 'City\t'
    header += 'Pincode\n'

    data = [
        {"Srno":'1','name':"Manas", 'email':"Manas@gmail.com",'addr':'BTM', 'city':'Bangalore', 'pin':'560090'},
        {"Srno": '2', 'name': "Balaj", 'email': "Balaj@gmail.com", 'addr': 'Silk Board', 'city': 'Pune', 'pin': '560091'},
        {"Srno": '3', 'name': "Srikant", 'email': "Srikant@gmail.com", 'addr': 'Bhalki', 'city': 'Chennai', 'pin': '560092'},
        {"Srno": '4', 'name': "Umakant", 'email': "Umakant@gmail.com", 'addr': 'Bidar', 'city': 'Hyderabad', 'pin': '560093'},
        {"Srno": '5', 'name': "Raj", 'email': "Raj@gmail.com", 'addr': 'Aurad', 'city': 'Bangalore', 'pin': '560090'}
    ]
    row = '';
    for i in data:
        row += i['Srno']+"\t"
        row += i['name']+"\t"
        row += i['email']+"\t"
        row += i['addr']+"\t"
        row += i['pin']+"\t"
        row += i['city']+"\n"
    data = User.objects.all()
    for i in data:
        print(i)
    response.write(header + row)
    return response

def profile_form(request):
    form = ProfileForn()
    if request.method == 'POST':
        form = ProfileForn(request.POST)
        if form.is_valid():
            # logger.error(form.cleaned_data['name'])
            profile = Profile()
            user = db_user()
            user.username = form.cleaned_data['name']
            user.email = form.cleaned_data['email']
            user.save()
            profile.address = form.cleaned_data['address']
            profile.city = form.cleaned_data['city']
            profile.created_at = datetime.today()
            profile.user_id = user
            profile.save()
            return redirect('index_emp')
    return render(request, 'profile/create.html', {'form': form})



def indexEmp(request):

    data = Employee1.objects.raw('select * from college_employee1')
    return render(request, 'emp1/index.html', {'data':data})

def createEmp(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            #logger.error(form.cleaned_data['name'])
            emp = Employee1()
            emp.name = form.cleaned_data['name']
            emp.email = form.cleaned_data['email']
            emp.address = form.cleaned_data['address']
            emp.save()
            return redirect('index_emp')
    return render(request, 'emp1/create.html', {'form': form})


def ajaxExample(request):

    name = request.GET.get('username')
    data = Student.objects.filter(name__iexact=name)
    name = False
    if data:
        name = True

    return HttpResponse(name)

def updateEmp(request,pk):
    data = Employee1.objects.get(pk=pk)
    form = EmployeeForm()
    #logger.error(data.name)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=data)
        if form.is_valid():
            emp = Employee1()
            emp.id = pk
            emp.name = form.cleaned_data['name']
            emp.email = form.cleaned_data['email']
            emp.address = form.cleaned_data['address']
            emp.save()
            return redirect('index_emp')
    form.fields['name'].initial = data.name
    form.fields['email'].initial = data.email
    form.fields['address'].initial = data.address
    return render(request, 'emp1/update.html', {'form': form})


def signUp(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            form = CreateUserForm()
            return render(request, 'sites/register.html', {'form': form, 'message': 1})
    return render(request, 'sites/register.html', {'form': form, 'message': ''})

def logout(request):
    auth_logout(request)
    return redirect('dashboard')



def signIn(request):

    request.session['hello'] = "i am here"

    if request.user.is_authenticated:
        return redirect('dashboard')

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session.set_expiry(0)
                return redirect('dashboard')
            return render(request, 'sites/login.html', {'form': form, 'error': 'User Not found!'})
    return render(request, 'sites/login.html', {'form': form, 'message': ''})


def dashboard(request):

    if request.user.is_authenticated:
        return render(request, 'sites/dashboard.html', {'user': request.user})
    return redirect('signIn')


@login_required(login_url='/collage/login')
def index(request):

    data = Employee.objects.all()
    return render(request, 'emp/index.html', {'data':data})


def update(request, pk):

    data = Employee.objects.get(id=pk)
    form = EmpForm(instance=data)
    if request.method == "POST":
        form = EmpForm(request.POST, request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('index')
    form.fields['email'].widget.attrs['readonly'] = True
    return render(request, 'emp/update.html', {'form': form})


def delete(request, pk):

    data = Employee.objects.get(id=pk)
    data.delete()
    return redirect("index")

def view(request, dk):
    try:
        data = Employee.objects.get(pk=dk)
    except Employee.DoesNotExist:
        return HttpResponse("User  not found!")
    return render(request, 'emp/view.html', {'data':data})

def paramRedi(request):

    return redirect('view', 7)

def create(request):

    form = EmpForm()
    if request.method == "POST":
        form = EmpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'emp/create.html', {'form': form})

def myForm(request):

    form = MyForm()
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            return render(request, 'myform.html', {'form':form})
    return render(request, 'myform.html', {'form': form})

def hello(request):

    return render(request, 'hello.html', {'l1':[1,'xyz',2,3,4,5],'num':1, 'username':"Manas"})

def hello_world(request):

    return render(request, 'hello2.html')

def createStudent(request):

    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_student')
    return render(request, 'student/create.html', {'form': form})


def updateStudent(request, pk):

    data = Student.objects.get(id=pk)

    form = StudentForm(instance=data)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('index_student')

    #form.fields['email'].widget.attrs['readonly'] = True
    return render(request, 'student/update.html', {'form': form})


def indexStudent(request):

    data = Student.objects.all()
    return render(request, 'student/index.html', {'data':data})

def deleteStudent(request, pk):

    data = Student.objects.get(id=pk)
    data.delete()
    return redirect('index_student')