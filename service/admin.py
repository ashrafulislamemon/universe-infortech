from django.contrib import admin
from .models import ServiceModel
# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
  list_display = ('name',)
admin.site.register(ServiceModel,ServiceAdmin)  