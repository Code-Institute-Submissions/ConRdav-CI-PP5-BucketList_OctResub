from django import forms
from .models import Testimonial


class TestimonialForm(forms.ModelForm):
    """ testimonial form """
    class Meta:
        """ testimonial form fields """
        model = Testimonial
        fields = '__all__'
