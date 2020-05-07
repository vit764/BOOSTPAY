from django.shortcuts import render
#from .forms import SubscriberForm
from products.models import *



def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category__id=4)
    products_images_laptops = products_images.filter(product__category__name="Dota2")
    #products = Product.objects.filter(is_active=True)
    categorys = ProductCategory.objects.all()
    return render(request, 'landing/home.html', locals())
