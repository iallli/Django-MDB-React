from dataclasses import fields
import imp
from pyexpat import model
from rest_framework import serializers
from Employ.models import Departments, Employees


class departmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('departmentId', 'departmentName')


class employeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('employId', 'employName', 'department', 'doj', 'photoName')
