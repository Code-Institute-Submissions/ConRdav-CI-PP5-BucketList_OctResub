from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    """ contact form """
    class Meta:
        """ contact form fields """
        model = Contact
        fields = '__all__'
