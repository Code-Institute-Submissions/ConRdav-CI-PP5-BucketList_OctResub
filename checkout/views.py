from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in youir bag at the moment")
        return redirect(reverse('adventures'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LeQcKJg5lsH5J6iibutuIijInoboyrrztWhMiQSev9UGFsaoy2uSqNWZLEAAh4IrSpGfvyxR1X4nmCtG2ssLiiu00umzLBS0h',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
