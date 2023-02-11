
from django.db import models

# Create your models here.
class User(models.Model):
    
    username=models.CharField(max_length=30)
    email= models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    pass1 = models.CharField(max_length=30)
    pass2 = models.CharField(max_length=30)
    
    
class stresults(models.Model):
    rnum = models.CharField(max_length=30)
    nme = models.CharField(max_length=30)
    dob = models.CharField(max_length=30)
    rslt = models.CharField(max_length=30)
    def __str__(self):
        return  (self.nme)
            

