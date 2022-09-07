from django.shortcuts import get_object_or_404
from adventures.models import Adventure


def bag_contents(request):
    """ A method to work out the shopping bag total """
    bag_items = []
    total = 0
    adventure_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            adventure = get_object_or_404(Adventure, pk=item_id)
            total += (item_data * adventure.price)
            adventure_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'adventure': adventure,
            })

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'adventure_count': adventure_count,
        'grand_total': grand_total,
    }

    return context
