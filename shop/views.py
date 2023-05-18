from django.shortcuts import render
from .models import Products, Category,Basket,BasketItem

def main_page(request, category_pk=None):

    if category_pk:
        category = Category.objects.all()
        content = Products.objects.filter(category=category_pk)
    else:
        category = Category.objects.all()
        content = Products.objects.all()
    return render(request,"shop/main_page.html",{"content":content, 'category':category})




def to_korzina(request, product_id = None):
    product = Product.objects.get(id=product_id)
    product.category = "Korzinka"
    product.save()
    print(product_id)
    return render(request,"shop/main_page.html",{"content":content, 'category':category})






def BasketView(request):
    basket = Basket.objects.filter(user=request.user).first()
    bas = basket
    product = basket.product.all().values()
    return render(request, "shop/basket.html",{"basket":basket,"product":product,"bas":bas,"total":Basket.get_total_price(basket)})

def BasketItemView(request):
    basket1 = BasketItem.objects.filter(user=request.user).first()
    bas1 = basket
    product1 = basket.product.all().values()
    return render(request, "shop/basket.html",{"basket1":basket1,"product1":product1,"bas1":bas,"total1":Basket.get_total_price(basket)})