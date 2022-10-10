from django import forms
from .models import Adventure, Excursion


class AdventureForm(forms.ModelForm):
    """ adventure form """
    class Meta:
        """ fields for adventure form """
        model = Adventure
        fields = '__all__'


class ExcursionForm(forms.ModelForm):
    """ excursion form """
    class Meta:
        """ fields for excursion form """
        model = Excursion
        fields = '__all__'
