from decimal import Decimal
from django.conf import settings

def bag_content(request):
    """ A method to work out the shopping bag total """
    bag_items = []
    total = 0
    product_count = 0

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count
    }

    return context
