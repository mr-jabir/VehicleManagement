from django.db import models

# Create your models here.
class vehicledb(models.Model):
    vname=models.CharField(max_length=100,null=True,blank=True)
    vtype=models.CharField(max_length=100,null=True,blank=True)
    vmodel=models.IntegerField(null=True,blank=True)
    vdescription=models.CharField(max_length=100,null=True,blank=True)

class userdb(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    confirmpassword = models.CharField(max_length=100, null=True, blank=True)

class admindb(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    confirmpassword = models.CharField(max_length=100, null=True, blank=True)
