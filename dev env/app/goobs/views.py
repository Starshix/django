from django.shortcuts import render

from goobs.models import Products

def catalog(request):
    
    goobs = Products.objects.all()

    context = {
        "title": "Home - Каталог",
        "goobs": goobs,
    }
    return render(request, "goobs/catalog.html", context)

def product(request):
    return render(request, "goobs/product.html")

