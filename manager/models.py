from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Manager(models.Model):
    fullname=models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    description = models.TextField
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.fullname

class Announcement(models.Model):
    description = models.CharField(max_length=1000)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, default=True)
    def __str__(self):
        return self.description
