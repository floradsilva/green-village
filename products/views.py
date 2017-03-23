from django.shortcuts import render
from .models import Product
from django.http import Http404

def products_list(request):
	products = []
	template = 'products/products.html'
	context = {}

	products = Product.objects.all()
	context['products'] = products
	context['image'] = 'products/coconut-small.jpg'

 	return render(request, template, context)


def product(request, product_id):
	context = {}
	template = 'products/product.html'
	try:
		product = Product.objects.get(id=product_id)
	except Product.DoesNotExist:
		raise Http404("Product does not exist")

	context['product'] = product

	return render(request, template, context)	