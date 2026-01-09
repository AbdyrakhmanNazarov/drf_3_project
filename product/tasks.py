from celery import shared_task
from .models import Cart

@shared_task
def calculate_cart_total(cart_id):
    try:
        cart = Cart.objects.get(id=cart_id)
        total = cart.total_price()
        print(f"Cart {cart_id} total: {total}")
        return total
    except Cart.DoesNotExist:
        return 0
