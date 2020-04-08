from django.contrib import admin
from .models import *


# Register your models here.

class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('dept_no', 'dept_name')


class DeptEmpAdmin(admin.ModelAdmin):
    list_display = ('emp_no', 'dept_no', 'from_date', 'to_date')


class DeptManagerAdmin(admin.ModelAdmin):
    list_display = ('emp_no', 'dept_no', 'from_date', 'to_date')


class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('emp_no', 'birth_date', 'first_name', 'last_name', 'gender', 'hire_date')


class SalariesAdmin(admin.ModelAdmin):
    list_display = ('emp_no', 'salary', 'from_date', 'to_date')


class TitlesAdmin(admin.ModelAdmin):
    list_display = ('emp_no', 'title', 'from_date', 'to_date')


admin.site.register(Departments, DepartmentsAdmin)
admin.site.register(DeptEmp, DeptEmpAdmin)
admin.site.register(DeptManager, DeptManagerAdmin)
admin.site.register(Employees, EmployeesAdmin)
admin.site.register(Salaries, SalariesAdmin)
admin.site.register(Titles, TitlesAdmin)
