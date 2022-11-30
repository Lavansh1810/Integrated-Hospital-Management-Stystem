from django.db import models
from datetime import datetime
from listings.models import Listing
import uuid

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    hospital = models.ManyToManyField(Listing)
    specs = models.CharField(max_length=200,default='Cardio')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    desc = models.TextField(blank=True)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date=models.DateTimeField(default=datetime.now,blank=True)
   

    def __str__(self):
        return '%s' % (self.name)

