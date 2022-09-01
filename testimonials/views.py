from django.shortcuts import render
from .models import Testimonial

# Create your views here.


def view_testimonials(request):
    """ A view to return the shopping bag """

    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'testimonials/testimonials.html', context)
