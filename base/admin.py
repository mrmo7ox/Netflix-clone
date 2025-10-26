from django.contrib import admin
from .models import *




class nuserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'address']  # Fields to display in the admin list view
    search_fields = ['email', 'name']  # Fields to enable searching in the admin interface
    list_filter = ['city', 'date']  # Fields to enable filtering in the admin interface
admin.site.register(nuser, nuserAdmin)

# Register your models here.


