from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    product_objects = Product.objects.all()
    #search code
    product_name = request.GET.get('product_name')
    if product_name != '' and product_name is not None:
        product_objects = Product.objects.filter(title__icontains=product_name)
    #pagination code
    paginator = Paginator(product_objects, 8)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_objects':product_objects})

def detail(request, id):
    product_object = Product.objects.get(id=id)
    related_products = Product.objects.filter(category=product_object.category).exclude(id=id)[:4]
    return render(request, 'shop/detail.html', {'product_object':product_object, 'related_products':related_products})