from django.contrib import admin

from .models import ItemModel

@admin.register(ItemModel)
class ItemModel(admin.ModelAdmin):
    pass
