from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField()
    password=models.CharField(max_length=20)