from statistics import mode
from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.
class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=25,null=True)
    email=models.EmailField(max_length=60,null=True)
    password=models.CharField(max_length=12,null=True)
    gender=models.CharField(max_length=100)
    city=models.CharField(max_length=100,null=True)
    resume=models.FileField(null=True)
    img=models.ImageField(null=True)
    
   
    def __str__(self) :
        return self.name
    
class File_Data(models.Model):
    files=models.FileField(upload_to='media')