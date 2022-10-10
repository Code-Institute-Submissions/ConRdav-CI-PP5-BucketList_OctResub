from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Testimonial
from .forms import TestimonialForm


def view_testimonials(request):
    """ A view to return the shopping bag """

    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'testimonials/testimonials.html', context)


def add_testimonial(request):
    """ Add a testimonial to testimonials page """

    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added testimonial!')
            return redirect('testimonials')
        else:
            messages.error(request, (
                'Failed to add testimonial. Please ensure the form is valid.'
                ))
    else:
        form = TestimonialForm()

    template = 'testimonials/add_testimonial.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
