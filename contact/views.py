from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """ Sends a enquiry to the admin """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message, [settings.EMAIL_HOST_USER],
                      [settings.EMAIL_HOST_USER])
            messages.success(request, 'Thank you for your enquiry!')
            return redirect('contact')
        else:
            messages.error(request, 'Failed to send enquiry. Please ensure the form is valid.')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'contact/contact.html', context)
