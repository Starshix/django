from django.contrib import admin

from goobs.models import Products

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}
    
