from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Booking(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    pin_code=models.CharField(max_length=30)
    description=models.TextField()
    date=models.DateField()
    author= models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=False)

class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    subject=models.CharField(max_length=30)
    message=models.TextField() 


class Review(models.Model):
    message=models.TextField()
    author= models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=False)

class Subscriber(models.Model):
    email=models.EmailField()

