from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
    )
from django.contrib import messages

from adventures.models import Adventure

# Create your views here.


def view_bag(request):
    """ A view to return the shopping bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified adventure to the shopping bag """

    adventure = Adventure.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, (
            f'Updated {adventure.name} quantity to {bag[item_id]}'
            ))
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {adventure.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified adventure to the shopping bag """

    adventure = get_object_or_404(Adventure, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, (
            f'Updated {adventure.name} quantity to {bag[item_id]}'
            ))
    else:
        bag.pop(item_id)
        messages.success(request, (
            f'Removed {adventure.name} quantity to {bag[item_id]}'
            ))

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the specified adventure from the shopping bag """

    adventure = get_object_or_404(Adventure, pk=item_id)
    bag = request.session.get('bag', {})

    bag.pop(item_id)
    messages.success(request, (
        f'Removed {adventure.name} adventure from your bag.'
        ))

    request.session['bag'] = bag
    return HttpResponse(status=200)
