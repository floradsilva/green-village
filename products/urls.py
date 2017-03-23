from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^products/$', views.products_list, name='products'),
	url(r'^$', views.products_list),
	url(r'^(?P<product_id>[0-9]+)/$', views.product, name='product'),
]