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


class AddTestimonial(View):
    """
    This class contains the get method to provide the testimonial post
    form to enable the user to create a testimonial post.
    This class contains the post method allowing the user to
    submit their testimonial.
    """

    def get(self, request, *args, **kwargs):
        """
        the get method which displays the blog post
        form to the user.
        """
        testimonial_form = TestimonialForm()
        context = {'testimonial_form': testimonial_form}
        return render(request, 'add_testimonial.html', context)


    def post(self, request, *args, **kwargs):
        """
        This post method submits the blog post
        to be accepted in the admin area.
        """

        testimonial_form = TestimonialForm(request.POST, request.FILES)

        if testimonial_form.is_valid():
            form = testimonial_form.save(commit=False)
            form.author = User.objects.get(username=request.user.username)
            form.slug = form.title.replace(" ", "-")
            messages.success(
                request, 'Your testimonial has been posted.'
            )
            form.save()
        return render(
            request,
            'add_testimonial.html',
            {
                "posted": True,
            },
        )
