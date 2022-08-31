from django.shortcuts import render, get_object_or_404
from .models import Adventure, Category, Excursion

# Create your views here.


def all_adventures(request):
    """ A view to show all adventures, including sorting and search queries """

    adventures = Adventure.objects.all()
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            adventures = adventures.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'adventures': adventures,
        'current_categories': categories,
    }

    return render(request, 'adventures/adventures.html', context)


def adventure_detail(request, adventure_id):
    """ A view to show adventure details """

    adventure = get_object_or_404(Adventure, pk=adventure_id)
    categories = adventure.category
    excursion = Excursion.objects.filter(category=categories)

    context = {
        'adventure': adventure,
        'excursion': excursion,
    }

    return render(request, 'adventures/adventure_detail.html', context)
