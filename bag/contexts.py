# from decimal import Decimal
# from django.conf import settings
from django.shortcuts import get_object_or_404
from adventures.models import Adventure, Excursion


def bag_contents(request):
    """ A method to work out the shopping bag total """
    bag_items = []
    total = 0
    totalA = 0
    product_count = 0
    productA_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Adventure, pk=item_id)
            productA = get_object_or_404(Excursion, pk=item_id)
            total += (item_data * product.price)
            totalA += (item_data * productA.price)
            product_count += item_data
            productA_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'productA': productA,
            })

    context = {
        'bag_items': bag_items,
        'total': total,
        'totalA': totalA,
        'product_count': product_count,
        'productA_count': productA_count,
    }

    return context
