from django.urls import path
from .views import ProductListView, CartView, AddToCartView

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product-list'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
]