from django.contrib import admin
from .models import ProjectModel,galleryModel
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
  list_display = ('name',)
admin.site.register(ProjectModel,ProjectAdmin)  


admin.site.register(galleryModel)