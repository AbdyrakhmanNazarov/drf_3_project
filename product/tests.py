from django.test import TestCase
from accounts.models import User
from .models import Product, Cart, CartItem

class ProductTest(TestCase):
    def test_product_creation(self):
        p = Product.objects.create(name="Test Product", price=10.5)
        self.assertEqual(p.name, "Test Product")
        self.assertTrue(p.is_active)

class CartTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="cart@example.com", password="123")
        self.product = Product.objects.create(name="Item", price=5)

    def test_cart_add_item(self):
        cart = Cart.objects.create(user=self.user)
        item = CartItem.objects.create(cart=cart, product=self.product, quantity=2)
        self.assertEqual(cart.total_price(), 10)