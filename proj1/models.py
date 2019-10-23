from django.db import models
#from django.conf.urls import url

# Create your models here. we can create any class
class from_Malegaon_College(models.Model):
    
    start_loc = models.CharField(max_length=30)
    
class from_MalegaonBK(models.Model):
    
    start_loc = models.CharField(max_length=30)


class from_Shardanagar(models.Model):
    
    start_loc = models.CharField(max_length=30)


class from_Baramati(models.Model):
    
    start_loc = models.CharField(max_length=30)


class feedback(models.Model):

    username = models.CharField(max_length=15)
    email_id = models.CharField(max_length=30)
    message = models.CharField(max_length=50)
