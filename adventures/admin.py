from django.contrib import admin
from .models import Adventure, Continent, Excursion, Country


class AdventureAdmin(admin.ModelAdmin):
    """ class for adventure admin """

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
    """ class for continent admin """

    list_display = (
        'name',
    )


class CountryAdmin(admin.ModelAdmin):
    """ class for country admin """

    list_display = (
        'name',
    )


class ExcursionAdmin(admin.ModelAdmin):
    """ class for excursions admin """

    list_display = (
        'name',
        'image',
    )


admin.site.register(Adventure, AdventureAdmin)
admin.site.register(Continent, ContinentAdmin)
admin.site.register(Excursion, ExcursionAdmin)
admin.site.register(Country, CountryAdmin)
