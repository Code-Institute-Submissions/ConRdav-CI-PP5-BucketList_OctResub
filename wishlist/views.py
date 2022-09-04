from django.shortcuts import render, redirect


def view_wishlist(request):

    return render(request, 'wishlist/wishlist.html')


def add_to_wishlist(request, item_id):
    """ Add an adventure to the wishlist """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    wishlist = request.session.get('wishlist', {})

    if item_id in list(wishlist.keys()):
        wishlist[item_id] = quantity
   
    request.session['wishlist'] = wishlist
    return redirect(redirect_url)
