from django.db import models
#from django.conf.urls import url

# Create your models here. we can create any class
class Data(models.Model):
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    nickname =  models.CharField(max_length=30)

class Check(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


