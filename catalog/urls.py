from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # url(r'^about/$', views.about, name='about'),



    url(r'^category/(?P<category_slug>[\w\-]+)/$', views.show_category, name='show_category'),

    url(r'^category/(?P<product_slug>[\w\-]+)/$', views.show_product, name='show_product'),



]
