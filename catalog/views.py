from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404,render,render_to_response
from .models import Category,Product
from django.template import  RequestContext
from django.core import urlresolvers
from cart import  cart
from django.http import HttpResponseRedirect
from cart.forms import ProductAddToCartForm


def index(request):
    page_title = 'Leather products and varieties'
    request_context = RequestContext(request)
    return render_to_response('catalog/index.html',locals(),context_instance=request_context)

def show_category(request,category_slug):

    request_context = RequestContext(request)
    c = get_object_or_404(Category,slug =category_slug)
    products = c.product_set.all()
    page_title = c.name
    mega_keywords = c.meta_keywords
    meta_description = c.meta_description

    return  render_to_response('catalog/category.html',locals(),request_context)

def show_product(request,product_slug):

    request_context = RequestContext(request)

    p = get_object_or_404(Product, slug = product_slug)
    categories = p.categories.filter(is_active = True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description

    if request.method == 'POST':
        postdata = request.POST.copy()
        form = ProductAddToCartForm(request,postdata)

        if form.is_valid():
            cart.add_to_cart(request)

            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()

            url = urlresolvers.reverse('show_cart')
            return (url)
        else:
            form = ProductAddToCartForm(request=request, label_suffix=':')
            form.fields['product_slug'].widget.attrs['value'] = product_slug

            request.session.set_test_cookie()
    return render_to_response('catalog/product.html',locals(),request_context)