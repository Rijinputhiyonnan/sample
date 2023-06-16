from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class courseModel(models.Model):
    course_name = models.CharField(max_length=270)


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="media/")
    course_name = models.ForeignKey(courseModel,on_delete=models.CASCADE,null=True)
    

class Student(models.Model):
    fname = models.CharField(max_length=255)
    lname= models.CharField(max_length=255)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    course_name = models.ForeignKey(courseModel,on_delete=models.CASCADE,null=True)
