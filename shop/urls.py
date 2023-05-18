from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path("",views.main_page,name="main_page"),
    path("<int:category_pk>",views.main_page,name="main_page_category"),
    path('<int:product_id>', views.to_korzina, name='change_category'),
    path('', views.BasketView, name='to_basket'),
    path('basket', views.BasketView, name='basket'),
]
