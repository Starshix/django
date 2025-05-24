from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to="goobs_image", blank=True, null=True, verbose_name="Изображение")
    price = models.DecimalField(default=0.00, max_digits=8, decimal_places=2, verbose_name="Цена")
    discount = models.DecimalField(default=0.00, max_digits=8, decimal_places=2, verbose_name="Скидка в процентах")

    class Mets:
        db_table = "product"
        verbose_name  = "Продукты"
        verbose_name_plural = "Продукт"

    def __str__(self):
        return self.name
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        
        return self.price