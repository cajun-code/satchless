from django.conf.urls.defaults import *
from . import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='satchless-product-index'),
        url(r'^(?P<parent_slugs>([a-z0-9_-]+/)*)(?P<category_slug>[a-z0-9_-]+)/$',
            views.category, name='satchless-product-category'),
        # this url simplifies url templatetag usage ({% url slug %} instead of {% url '' slug %})
        url(r'^(?P<category_slug>[a-z0-9_-]+)/$',
            views.category, name='satchless-product-category'),
        # '+' which predeces product slug prevents conflicts with categories paths
        url(r'^(?P<category_slugs>([a-z0-9_-]+/)+)\+(?P<product_slug>[a-z0-9_-]+)/$',
            views.product, name='satchless-product-product'),
        url(r'^\+(?P<product_slug>[a-z0-9_-]+),(?P<product_pk>[0-9]+)/$',
            views.product, name='satchless-product-product'),
        )
