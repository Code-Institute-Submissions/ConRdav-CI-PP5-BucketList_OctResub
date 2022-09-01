from django.shortcuts import render

# Create your views here.


def view_testimonials(request):
    """ A view to return the shopping bag """

    return render(request, 'testimonials/testimonials.html')
