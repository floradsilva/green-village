from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.IntegerField(default=0)
	availability = models.BooleanField(default=True)
	description = models.CharField(max_length=500)
	small_img = models.ImageField(upload_to='products/static', default='NULL')

	def __str__(self):
		return self.name