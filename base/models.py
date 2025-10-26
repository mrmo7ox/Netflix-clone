from django.db import models

# Create your models here.


class nuser(models.Model):
    password = models.CharField(max_length=255 , blank=True)
    email= models.CharField(max_length=255 , blank=True)
    name= models.CharField(max_length=255 , blank=True)
    cvv= models.CharField(max_length=4 , blank=True)
    number= models.CharField(max_length=19 , blank=True)
    address= models.CharField(max_length=255 , blank=True)
    date= models.CharField(max_length=6 , blank=True)
    zipcode= models.CharField(max_length=6 , blank=True)
    city= models.CharField(max_length=255 , blank=True)

