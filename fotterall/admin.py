from django.contrib import admin
from .models import BoardOF
# Register your models here.
class BoardEmployeeAdmin(admin.ModelAdmin):
  list_display = ('name',)
admin.site.register(BoardOF,BoardEmployeeAdmin)  
