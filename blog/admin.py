from django.contrib import admin
from .models import Item, ItemImage,Settings,Skill


class ItemImageInline(admin.TabularInline):
    model = ItemImage


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title','category','status','slug']
    list_editable = ['category','status']
    inlines = [
        ItemImageInline
    ]


class SkillInline(admin.TabularInline):
    model = Skill


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['phone','about']
    inlines = [
        SkillInline
    ]

