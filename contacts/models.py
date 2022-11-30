from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from listings.models import Listing

STATUS_CHOICES = (
    ('Pending','Pending'),
    ('Confirmed', 'Confirmed'),
    ('Completed','Completed'),
)

class Contacts(models.Model):
    listings = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.TextField(max_length=12)
    doctor = models.CharField(max_length=200,blank=True,null=True)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Pending')
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    appointment_date = models.DateTimeField(null=True,blank=True)
    user_id = models.IntegerField(blank = True)
    age = models.IntegerField(null=True,blank = True)
    amount = models.FloatField(null=True,blank = True)

    def username(self):

        user = User.objects.get(id=self.user_id)

        return user.username

    def hospital_name(self):

        hospital = Listing.objects.get(id=self.listing_id)

        return hospital.title

    def __str__(self):
        return self.name


