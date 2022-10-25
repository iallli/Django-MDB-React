from pyexpat import model
from django.db import models

# Create your models here.


class Departments(models.Model):
    departmentId = models.AutoField(primary_key=True)
    departmentName = models.CharField(max_length=500)


class Employees(models.Model):
    employId = models.AutoField(primary_key=True)
    employName = models.CharField(max_length=500)
    department = models.CharField(max_length=500)
    doj = models.DateField()
    photoName = models.CharField(max_length=500)
