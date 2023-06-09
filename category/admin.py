from django.contrib import admin
from .models import Category


@admin.register(Category)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title','parent','slug']
    list_editable = ['parent']

