from django.urls import path
from goobs import views


app_name = "goobs"

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]
