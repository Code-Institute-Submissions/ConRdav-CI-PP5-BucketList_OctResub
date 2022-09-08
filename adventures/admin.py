from django.contrib import admin
from .models import Adventure, Continent, Excursion, Country

# Register your models here.

class AdventureAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'continent',
        'price',
        'country',
        'continent',
        'theme',
        'image',
    )

class ContinentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

class CountryAdmin(admin.ModelAdmin):
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
admin.site.register(Continent, ContinentAdmin)
admin.site.register(Excursion, ExcursionAdmin)
admin.site.register(Country, CountryAdmin)

