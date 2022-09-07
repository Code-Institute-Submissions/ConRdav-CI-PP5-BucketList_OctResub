from django import forms
from .models import Adventure, Category, Country, Excursion


class AdventureForm(forms.ModelForm):

    class Meta:
        model = Adventure
        fields = '__all__'

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'  

class CountryForm(forms.ModelForm):

    class Meta:
        model = Country
        fields = '__all__'

class ExcursionForm(forms.ModelForm):

    class Meta:
        model = Excursion
        fields = '__all__'
