from django.contrib import admin
from .models import CustomerItem, CustomerItemImage


class CustomerImageInline(admin.TabularInline):
    model = CustomerItemImage


@admin.register(CustomerItem)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('title','slug')
    inlines = [
        CustomerImageInline
    ]
