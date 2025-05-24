from django.shortcuts import render

from goobs.models import Products

def catalog(request):
    
    goobs = Products.objects.all()

    context = {
        "title": "Home - Каталог",
        "goobs": goobs,
    }
    return render(request, "goobs/catalog.html", context)

def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        "product": product
    }
    return render(request, "goobs/product.html", context=context)

