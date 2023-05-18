from django.contrib import admin
from .models import Products,Category,Basket,BasketItem
admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Basket)
admin.site.register(BasketItem)