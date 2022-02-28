from distutils.command.upload import upload
from statistics import mode
from django.db import models
from django.urls import reverse
# Create your models here.
class ServiceModel(models.Model):
  name=models.CharField(max_length=200,unique=True)
  slug=models.SlugField(max_length=200,null=False,unique=True)
  image=models.ImageField(upload_to='photos/service')

  def __str__(self):
        return self.name

  def get_url(self):

    return reverse ('servicedetails',kwargs={"servicemodel_slug":self.slug}) 


  