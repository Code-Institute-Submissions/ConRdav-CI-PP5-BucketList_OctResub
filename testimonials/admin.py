from django.contrib import admin
from .models import Testimonial

# Register your models here.


class TestimonialAdmin(admin.ModelAdmin):
    """ view testimonials in admin """ 
    list_display = (
        'country',
        'user',
        'pub_date',
        'comment',
        'value',
    )


admin.site.register(Testimonial, TestimonialAdmin)
