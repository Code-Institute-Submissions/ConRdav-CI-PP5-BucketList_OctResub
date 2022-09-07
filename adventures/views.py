from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Adventure, Category, Excursion
from .forms import AdventureForm

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
    # if not user.is_superuser:
    #     messages.error(request, 'Sorry, only store owners can do that.')
    #     return redirect(reverse('index'))

    if request.method == 'POST':
        form = AdventureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added adventure!')
            return redirect ('adventures')
        else:
            messages.error(request, 'Failed to add adventure. Please ensure the form is valid.')
    else:
        form = AdventureForm()

    template = 'adventures/add_adventure.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_adventure(request, adventure_id):
    # """ Edit an adventure in the store """
    # if not user.is_superuser:
    #     messages.error(request, 'Sorry, only store owners can do that.')
    #     return redirect(reverse('index'))

    adventure = get_object_or_404(Adventure, pk=adventure_id)
    if request.method =='POST':
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
    # if not user.is_superuser:
    #     messages.error(request, 'Sorry, only store owners can do that.')
    #     return redirect(reverse('index'))

    adventure = get_object_or_404(Adventure, pk=adventure_id)
    adventure.delete()
    messages.success(request, 'Adventure deleted!')
    return redirect(reverse('adventures'))
