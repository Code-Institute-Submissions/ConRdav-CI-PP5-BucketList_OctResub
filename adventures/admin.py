from django.contrib import admin
from .models import Adventure, Category

# Register your models here.

class AdventureAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'country',
        'continent',
        'theme',
        'image',
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

admin.site.register(Adventure, AdventureAdmin)
admin.site.register(Category, CategoryAdmin)

