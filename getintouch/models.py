from statistics import mode
from django.db import models

from django.urls import reverse

# Create your models here.
class Employee(models.Model):
  name=models.CharField(max_length=200)
  image=models.ImageField(upload_to='photos/employee')
  employee_post=models.CharField(max_length=200)


  def __str__(self):
        return self.name


class CarrerModel(models.Model):
  job_post=models.CharField(max_length=200)
  slug=models.SlugField(max_length=200,null=False,unique=True)
  sallery=models.CharField(max_length=200)
  postedat=models.CharField(max_length=200)


  def __str__(self):
        return self.job_post

  def get_url(self):

    return reverse ('carrerdetails',kwargs={"carrermodel_slug":self.slug}) 


    
      
