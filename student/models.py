from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    enrolled_course = models.CharField(max_length=100, default='CSIT')
    contact_number = models.CharField(max_length=100)
    is_first_login = True
    is_suspended = True
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.fullname

    class Class(models.Model):
        student_name = models.CharField(max_length=100,null=True,blank=True)
        rollno = models.IntegerField()
        assignment = models.FileField()

