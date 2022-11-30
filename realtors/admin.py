from django.contrib import admin

from .models import Doctor

class RealtorsAdmin(admin.ModelAdmin):
    list_display= ('name','desc','is_mvp')
    list_display_links= ('name','desc')
    search_fields=('name','phone','email','desc')
    list_filter=('hospital',)
    list_editable=('is_mvp',)
    list_per_page=25

admin.site.register(Doctor,RealtorsAdmin)