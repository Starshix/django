from django.shortcuts import render

# Create your views here.

def catalog(request):
    return render(request, "goobs/catalog.html")

def product(request):
    return render(request, "goobs/product.html")
