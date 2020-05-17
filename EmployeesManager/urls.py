"""EmployeesManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from Managers.views import *

router = routers.DefaultRouter()
router.register('Departments', DepartmentsViews)
router.register('DeptEmp', DeptEmpViews)
router.register('DeptManager', DeptManagerViews)
router.register('Employees', EmployeesViews)
router.register('Salaries', SalariesViews)
router.register('Titles', TitlesViews)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/employeesList/', all_employees),
    # path('api/employeesList/username=<username>/password=<password>/', all_employees, name='all-employees-page'),
    path('api/employeesList/emp_no=<int:emp_no>/', single_employee),
    # path('api/employeesList/username=<username>/password=<password>/emp_no=<int:emp_no>/', single_employee,
    #      name='single-employee-page'),
    path('api/employeesListJustJSON/', all_employees_just_json),
    # path('api/employeesListJustJSON/', all_employees_just_json, name='all-employees-just-json-page'),
    path('api/createEmployee/', create_record),
    # path('api/createEmployee/', post_record, name='post-record-page'),
    # path(
    #     'api/updateEmployee/?emp_no=<int:emp_no>&first_name=<str:first_name>&last_name=<str:last_name>&gender=<str:gender>&birth_date=<str:birth_date>&hire_date=<str:hire_date>/',
    #     update_record),
    path('api/updateEmployee/info=<str:info>', update_record),
    path('api/deleteEmployee/emp_no=<int:emp_no>/', delete_employee_record),
    # path('api/deleteEmployee/emp_no=<int:emp_no>/', delete_employee_record, name='delete-employee-record-page'),
    path('api/searchEmployee/', get_employee_record),
    path('', get_employee_record),
    # path('api/searchEmployee/', get_employee_record, name='get-employee-record-page'),
    path('api/googleSearch/', google_search),
    # path('api/googleSearch/', google_search, name='google-search-page'),
    path('api/contact/', contact),
    # path('api/contact/', contact, name='contact-page'),
]
