from uuid import uuid4
from datetime import datetime

from django.test import TestCase
from store.models import Cart


class CartTestCase(TestCase):
    my_uuid = uuid4()

    def setUp(self) -> None:
        Cart.objects.create(id=self.my_uuid, created_at=datetime.now())

    def test_cart_creation(self):
        # Test create Cart
        cart = Cart.objects.get(id=self.my_uuid)
        self.assertIsInstance(cart, Cart)
