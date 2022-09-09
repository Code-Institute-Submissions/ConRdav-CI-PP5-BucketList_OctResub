from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """ Sends a enquiry to the admin """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your enquiry the we will get back to you asap!')
            return redirect('contact')
        else:
            messages.error(request, 'Failed to send enquiry. Please ensure the form is valid.')
    else:
        form = ContactForm()
     
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
