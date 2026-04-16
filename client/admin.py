from django.contrib import admin
from .models import Client
# Register your models here.
# admin.py
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phoneNumber', 'createdAt')

admin.site.register(Client, ClientAdmin)