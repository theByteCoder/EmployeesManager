from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets

from .forms import *
from .serializer import *


# Create your views here.
def get_last_employee_number():
    all_emp = Employees.objects.all().values()
    all_emp_list = list(all_emp)
    last_emp_record = all_emp_list[len(all_emp_list) - 1]
    return last_emp_record["emp_no"]


def all_employees(request):
    # def all_employees(request, username, password):
    # user = authenticate(username=username, password=password)
    # if user is not None:
    all_emp = Employees.objects.all()[:10]
    return render(request, 'index.html', {'all_emp': all_emp})


# else:
#     return render(request, 'permissions.html')


# # return JSON
def all_employees_just_json(request):
    all_emp = Employees.objects.all().values()[:10]
    all_emp_list = list(all_emp)
    print(all_emp_list)
    return JsonResponse(all_emp_list[len(all_emp_list) - 1], safe=False)


def single_employee(request, emp_no):
    # def single_employee(request, username, password, emp_no):
    # user = authenticate(username=username, password=password)
    # if user is not None:
    all_emp = list(Employees.objects.all().values().filter(emp_no=emp_no))
    if not (len(all_emp) == 0):
        return render(request, 'index.html', {'all_emp': all_emp})
        # return JsonResponse(all_emp_list, safe=False)
    else:
        return render(request, 'index.html', {'all_emp': []})


# else:
#     return render(request, 'permissions.html')


def google_search(request):
    return render(request, 'googlesearch.html', {})


def post_record(request):
    form = EmployeesForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            Employees.objects.create(**form.cleaned_data)
            form = EmployeesForm()
        else:
            print(form.errors)
    return render(request, 'createrecord.html', {'form': form})


def create_record(request, emp_no, birth_date, first_name, last_name, gender, hire_date):
    import json
    details = json.loads(info['info'])
    all_emp = Employees(emp_no=details['emp_no'], birth_date=details['birth_date'], first_name=details['first_name'],
                        last_name=details['last_name']
                        , gender=details['gender'], hire_date=details['hire_date'])
    all_emp.save()
    return render(request, 'createrecord.html', {})


def update_record(request, **info):
    import json
    details = json.loads(info['info'])
    print(details)
    all_emp = Employees(emp_no=details['emp_no'], birth_date=details['birth_date'], first_name=details['first_name'],
                        last_name=details['last_name']
                        , gender=details['gender'], hire_date=details['hire_date'])
    all_emp.save()
    return render(request, 'editrecord.html', {})


# def update_record(request, emp_no, birth_date, first_name, last_name, gender, hire_date):
#     all_emp = Employees(emp_no=emp_no, birth_date=birth_date, first_name=first_name,
#                         last_name=last_name
#                         , gender=gender, hire_date=hire_date)
#     all_emp.save()
#     return render(request, 'editrecord.html', {})

# def request_name(request):
#     if request.method == "POST" and 'search' in request.POST:
#         get_employee_record(request)
#     elif request.method == "POST" and 'update' in request.POST:
#         update_record()

def search_employee_record(request, emp_no):
    if emp_no == "*":
        record = list(Employees.objects.all()[:10000])
    else:
        record = list(Employees.objects.all().values().filter(emp_no=emp_no))
    return render(request, 'searchrecord.html', {'record': record})


def get_employee_record(request):
    # form = EmployeesFormToDelete(request.POST or None)
    record = []
    if request.method == "POST":
        emp_no = request.POST.get("emp_no", None)
        if emp_no == "*":
            # record = list(Employees.objects.all()[:100])
            record = list(Employees.objects.all()[:1000])
        else:
            record = list(Employees.objects.all().values().filter(emp_no=emp_no))
    return render(request, 'searchrecord.html', {'record': record})


def delete_employee_record(request, emp_no):
    if emp_no != "" and type(emp_no) is not None:
        instance = Employees.objects.filter(emp_no=emp_no)
        instance.delete()
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
