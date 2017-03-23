from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^products/$', views.products_list, name='products'),
	url(r'^$', views.products_list, name='products'),
]