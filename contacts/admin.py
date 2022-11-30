from django.contrib import admin
from django.contrib.auth.models import User

from .models import Contacts

class ContactAdmin(admin.ModelAdmin):

    list_display = ('id','name', 'age', 'email','username','hospital_name','status','appointment_date','amount')
    list_display_links = ('id','name', 'age', 'email','username','hospital_name')
    list_editable=('status','appointment_date','amount',)
    search_field = ('name', 'email','username',)
    list_filter = ('listings',)

admin.site.register(Contacts, ContactAdmin)
