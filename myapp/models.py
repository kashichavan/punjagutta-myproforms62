from django.db import models

# Create your models here.

class StudentModel(models.Model):
    email=models.EmailField()
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    age=models.IntegerField()
    

