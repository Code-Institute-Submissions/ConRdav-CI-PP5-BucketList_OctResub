from django.contrib import admin
from .models import Adventure, Category, Excursion

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

class ExcursionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'image',
    )

admin.site.register(Adventure, AdventureAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Excursion, ExcursionAdmin)

