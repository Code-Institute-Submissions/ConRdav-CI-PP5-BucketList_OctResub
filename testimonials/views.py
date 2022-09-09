from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Testimonial
from .forms import TestimonialForm

# Create your views here.


def view_testimonials(request):
    """ A view to return the shopping bag """

    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'testimonials/testimonials.html', context)


def add_testimonial(request):
    """ Add a testimonial to testimonials page """
    # if not user.is_superuser:
    #     messages.error(request, 'Sorry, only store owners can do that.')
    #     return redirect(reverse('index'))

    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added testimonial!')
            return redirect('testimonials')
        else:
            messages.error(request, 'Failed to add testimonial. Please ensure the form is valid.')
    else:
        form = TestimonialForm()

    template = 'testimonials/add_testimonial.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_testimonial(request, user_id):
    """ Edit a testimonial in the store """

    testimonial = get_object_or_404(Testimonial, pk=user_id)
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated testimonial!')
            return redirect(reverse('testimonials')
        else:
            messages.error(request, 'Failed to update testimonial. please ensure the form is valid.')
    else:
        form = TestimonialForm(instance=adventure)
        messages.info(request, f'You are editing {testimonial.user} testimonial.')

    template = 'testimonials/edit_testimonial.html'
    context = {
        'form': form,
        'testimonial': testimonial
    }

    return render(request, template, context)


def delete_testimonial(request, user_id):
    """ Delete an adventure in the store """

    testimonial = get_object_or_404(Testimonial, pk=user_id)
    testimonial.delete()
    messages.success(request, 'Adventure deleted!')
    return redirect(reverse('adventures'))
