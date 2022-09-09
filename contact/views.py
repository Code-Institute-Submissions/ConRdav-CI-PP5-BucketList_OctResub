from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Contact
from .forms import ContactForm


def view_contacts(request):
    """ A view to return the enquiries """

    contacts = Contact.objects.all()

    context = {
        'contacts': contacts,
    }

    return render(request, 'contact/view_contacts.html', context)


def contact(request):
    """ Sends a enquiry to the admin """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your enquiry!')
            return redirect('contact')
        else:
            messages.error(request, 'Failed to send enquiry. Please ensure the form is valid.')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'contact/contact.html', context)
