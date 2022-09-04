from django.shortcuts import get_object_or_404
from adventures.models import Adventure


def wishlist_contents(request):
    """ A method to work out the shopping bag total """
    wishlist_items = []
    wishlist = request.session.get('wishlist', {})

    for item_id, item_data in wishlist.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Adventure, pk=item_id)
            wishlist_items.append({
                'item_id': item_id,
                'product': product,
            })

    context = {
        'wishlist_items': wishlist_items,
    }

    return context
