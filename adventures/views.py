from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Adventure, Continent, Excursion
from .forms import AdventureForm, ExcursionForm

# Create your views here.


def all_adventures(request):
    """ A view to show all adventures, including sorting and search queries """

    adventures = Adventure.objects.all()
    continents = None

    if request.GET:
        if 'continent' in request.GET:
            continents = request.GET['continent'].split(',')
            adventures = adventures.filter(continent__name__in=continents)
            continents = Continent.objects.filter(name__in=continents)

    context = {
        'adventures': adventures,
        'current_continents': continents,
    }

    return render(request, 'adventures/adventures.html', context)


def adventure_detail(request, adventure_id):
    """ A view to show adventure details """

    adventure = get_object_or_404(Adventure, pk=adventure_id)
    request.session['adventure_id'] = adventure.id

    context = {
        'adventure': adventure,
    }

    return render(request, 'adventures/adventure_detail.html', context)


def excursion_detail(request, country):
    """ A view to show excursion details """

    excursions = Excursion.objects.all()
    excursions = excursions.filter(country__name__contains=country)
    adventure_id = request.session.get('adventure_id', None)

    context = {
        'excursions': excursions,
        'adventure_id': adventure_id
    }

    return render(request, 'adventures/excursion_detail.html', context)


@login_required
def add_adventure(request):
    """ Add an adventure to the store """

    if request.method == 'POST':
        form = AdventureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added adventure!')
            return redirect('adventures')
        else:
            messages.error(request, ('Failed to add adventure. Please ensure the form is valid.')
    else:
        form = AdventureForm()

    template = 'adventures/add_adventure.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_adventure(request, adventure_id):
    """ Edit an adventure in the store """

    adventure = get_object_or_404(Adventure, pk=adventure_id)
    if request.method == 'POST':
        form = AdventureForm(request.POST, request.FILES, instance=adventure)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated adventure!')
            return redirect(reverse('adventure_detail', args=[adventure.id]))
        else:
            messages.error(request, 'Failed to update adventure. please ensure the form is valid.')
    else:
        form = AdventureForm(instance=adventure)
        messages.info(request, f'You are editing {adventure.name}')

    template = 'adventures/edit_adventure.html'
    context = {
        'form': form,
        'adventure': adventure
    }

    return render(request, template, context)


@login_required
def delete_adventure(request, adventure_id):
    """ Delete an adventure in the store """

    adventure = get_object_or_404(Adventure, pk=adventure_id)
    adventure.delete()
    messages.success(request, 'Adventure deleted!')
    return redirect(reverse('adventures'))


@login_required
def add_excursion(request):
    """ Add an excursion to the store """

    if request.method == 'POST':
        form = ExcursionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added an excursion!')
            return redirect('adventures')
        else:
            messages.error(request, 'Failed to add an excursion. Please ensure the form is valid.')
    else:
        form = ExcursionForm()

    template = 'adventures/add_excursion.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
