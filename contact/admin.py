from django.contrib import admin
from .models import ContactModel


@admin.register(ContactModel)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['subject','email','message']

