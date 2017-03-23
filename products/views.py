from django.shortcuts import render
from .models import Product

def products_list(request):
	products = []
	template = 'products/products.html'
	context = {}

	products = Product.objects.all()
	context['products'] = products
	context['image'] = 'products/coconut-small.jpg'

 	return render(request, template, context)


