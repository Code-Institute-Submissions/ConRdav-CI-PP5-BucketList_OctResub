from django import forms
from .models import Adventure, Category


class AdventureForm(forms.ModelForm):

    class Meta:
        model = Adventure
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()

     
  
