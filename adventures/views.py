from django.shortcuts import render
from .models import Adventure

# Create your views here.
def all_adventures(request):
    """ A view to show all adventures, including sorting and search queries """

    adventures = Adventure.objects.all()

    context = {
        'adventures': adventures,
    }

    return render(request, 'adventures/adventures.html', context)