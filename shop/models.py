from django.db import models


class Products(models.Model):
    product = models.CharField(max_length=255)
    definition = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField()
    category = models.ForeignKey(to = "Category", on_delete = models.CASCADE,blank=True)

    def __str__(self):
        return f"{self.id},{self.product}"
    
class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Basket(models.Model):
    product = models.ManyToManyField('Products',related_name="product_basket")
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)


    def add_to_basket(self, product):
        cart_item, created = CartItem.objects.get_or_create(cart=self, product=product)
        cart_item.quantity += quantity
        cart_item.save()

    def remove_from_basket(self, product):
        cart_item = CartItem.objects.get(cart=self, product=product)
        cart_item.delete()

    def clear_basket(self):
        self.product.clear()

    def get_total_price(self):
        return sum(item.product.price * item.quantity for item in self.basket_items.all())



    def __str__(self):
        return str(self.user)


class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='basket_items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return str(self.basket)