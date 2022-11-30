from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display=('title','city','state','pincode','estb','is_published','is_best',)
    list_display_links=('title',)
    list_editable=('is_published','is_best')
    search_fields=('title','description','address','city','state','pincode')
    list_per_page=25
 
admin.site.register(Listing,ListingAdmin)