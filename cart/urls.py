from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_cart, name='show_cat'),

    # url(r'^about/$', views.about, name='about'),






]
