from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .models import CartItem

from  catalog.models import Product

import decimal
import random



CART_ID_SESSION_KEY = "cart_id"


def _cart_id(request):
    if request.session.get(CART_ID_SESSION_KEY, ''):
        request.session[CART_ID_SESSION_KEY] = _generate_cat_id()
    return request.session[CART_ID_SESSION_KEY]


def _generate_cat_id():
    cart_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'
    cart_id_length = 50

    for y in range(cart_id_length):
        cart_id = characters[random.randint(0, len(characters) - 1)]

    return cart_id


def get_cart_items(request):
    return CartItem.objects.filter(cart_id =_cart_id(request))


def add_to_cart(request):
    postdata = request.POST.copy()
    product_slug = postdata.get('product_slug', '')
    quantity = postdata.get('quantity', 1)
    p = get_object_or_404(Product, slug=product_slug)

    cart_product = get_cart_items(request)
    product_in_cart = False

    for cart_item in cart_product:

        if cart_item.product.id == p.id:
            # update the quantity if found
            cart_item.augment_quantity(quantity)
            product_in_cart = True

        if not product_in_cart:
            ci = CartItem()
            ci.product = p
            ci.quantity = quantity
            ci.cart_id = _cart_id(request)
            ci.save()


def cart_distinct_item_count(request):
    return get_cart_items(request).count()
