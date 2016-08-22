from django.db import models

from django.contrib.auth.models import *

from django.utils import timezone

class Shirt(models.Model):
    EXTRA_LARGE ='XL'
    LARGE = 'L'
    MEDIUM = 'M'
    SMALL = 'S'
    SIZES = ((EXTRA_LARGE,'XL'),
             (LARGE,'L'),
             (MEDIUM,'M'),
             (SMALL,'S'),
             )
    
    id  = models.IntegerField(primary_key=True)
    #seller = models.ForeignKey(auth.user)
    price = models.IntegerField()
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=10)
    type = models.CharField(max_length=20)
    material = models.CharField(max_length=20)
    size  = models.CharField(max_length=2,choices=SIZES,default=MEDIUM,)

class T_shirt(models.Model):

    EXTRA_LARGE ='XL'
    LARGE = 'L'
    MEDIUM = 'M'
    SMALL = 'S'
    SIZES = ((EXTRA_LARGE,'XL'),
             (LARGE,'L'),
             (MEDIUM,'M'),
             (SMALL,'S'),
             )
    
    t_shirt_id = models.IntegerField(primary_key=True)
    #seller = models.ForeignKey(auth.user)
    selling_price = models.IntegerField()
    t_shirt_name = models.CharField(max_length=100)
    t_shirt_brand = models.CharField(max_length=100)
    t_shirt_color = models.CharField(max_length=10)
    t_shirt_type = models.CharField(max_length=20)
    t_shirt_material = models.CharField(max_length=20)
    t_shirt_size  = models.CharField(max_length=2,choices=SIZES,default=MEDIUM,)

class Company(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=150)

    
    
