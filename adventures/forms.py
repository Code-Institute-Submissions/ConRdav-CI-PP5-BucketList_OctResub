from django import forms
from .models import Adventure, Excursion


class AdventureForm(forms.ModelForm):

    class Meta:
        model = Adventure
        fields = '__all__'


class ExcursionForm(forms.ModelForm):

    class Meta:
        model = Excursion
        fields = '__all__'
