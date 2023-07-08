from django.contrib import admin
from .models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['name','email','password', 'gender', 'city', 'resume', 'img']


admin.site.register(Employee,EmployeeAdmin)