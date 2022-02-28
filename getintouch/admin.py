from django.contrib import admin
from .models import Employee,CarrerModel
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
  list_display = ('name',)
admin.site.register(Employee,EmployeeAdmin)  

class CarrerEmployeeAdmin(admin.ModelAdmin):
  list_display = ('job_post','sallery','postedat')
admin.site.register(CarrerModel,CarrerEmployeeAdmin)  
