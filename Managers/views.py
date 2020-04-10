from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets

from .forms import *
from .serializer import *


# Create your views here.
def all_employees(request, username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        all_emp = Employees.objects.all()[:10]
        return render(request, 'index.html', {'all_emp': all_emp})
    else:
        return render(request, 'permissions.html')


# # return JSON
def all_employees_just_json(request):
    all_emp = Employees.objects.all().values()[:10]
    all_emp_list = list(all_emp)
    return JsonResponse(all_emp_list, safe=False)


def single_employee(request, username, password, emp_no):
    user = authenticate(username=username, password=password)
    if user is not None:
        all_emp = list(Employees.objects.all().values().filter(emp_no=emp_no))
        if not (len(all_emp) == 0):
            return render(request, 'index.html', {'all_emp': all_emp})
            # return JsonResponse(all_emp_list, safe=False)
        else:
            return render(request, 'index.html', {'all_emp': []})
    else:
        return render(request, 'permissions.html')


def google_search(request):
    return render(request, 'googlesearch.html', {})


def post_record(request):
    form = EmployeesForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print(form.cleaned_data)
            Employees.objects.create(**form.cleaned_data)
            form = EmployeesForm()
        else:
            print(form.errors)
    return render(request, 'createrecord.html', {'form': form})


def get_employee_record(request):
    # form = EmployeesFormToDelete(request.POST or None)
    record = []
    if request.method == "POST":
        emp_no = request.POST.get("emp_no", None)
        if emp_no == "*":
            record = list(Employees.objects.all()[:100])
        else:
            record = list(Employees.objects.all().values().filter(emp_no=emp_no))
    return render(request, 'searchrecord.html', {'record': record})


def delete_employee_record(request, emp_no):
    if emp_no != "" and type(emp_no) is not None:
        instance = Employees.objects.filter(emp_no=emp_no)
        instance.delete()
        print(emp_no)
    return render(request, 'deleterecord.html', {'emp_no': emp_no})


def contact(request, *args, **kwargs):
    print(request.user)
    return HttpResponse("<h1>Contacts</h1>")


# # creates new entry
# def post_employee(request, user, pwd, **kwargs):
#     user = authenticate(username=user, password=pwd)
#     if user is not None:
#         all_emp = Employees(emp_no=kwargs['emp_no'], birth_date=kwargs['birth_date'], first_name=kwargs['first_name'],
#                             last_name=kwargs['last_name']
#                             , gender=kwargs['gender'], hire_date=kwargs['hire_date'])
#         all_emp.save()


class DepartmentsViews(viewsets.ModelViewSet):
    serializer_class = DepartmentsSerializer
    queryset = Departments.objects.all()


class DeptEmpViews(viewsets.ModelViewSet):
    serializer_class = DeptEmpSerializer
    queryset = DeptEmp.objects.all()


class DeptManagerViews(viewsets.ModelViewSet):
    serializer_class = DeptManagerSerializer
    queryset = DeptManager.objects.all()


class EmployeesViews(viewsets.ModelViewSet):
    serializer_class = EmployeesSerializer
    queryset = Employees.objects.all()


class SalariesViews(viewsets.ModelViewSet):
    serializer_class = SalariesSerializer
    queryset = Salaries.objects.all()


class TitlesViews(viewsets.ModelViewSet):
    serializer_class = TitlesSerializer
    queryset = Titles.objects.all()
