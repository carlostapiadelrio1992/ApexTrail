from django.test import TestCase
from django.urls import reverse
from store.models import Category, Product
from orders.models import Order, OrderItem


class OrderTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Senderismo', slug='senderismo')
        self.product = Product.objects.create(
            category=self.category,
            name='Terrex Free Hiker 2.0',
            slug='terrex-free-hiker-20',
            description='Bota senderismo',
            price=240000,
            sizes=[39, 40, 41],
            available=True
        )

    def test_order_creation_flow(self):
        # Add item to cart first
        self.client.post(
            reverse('cart:cart_add', args=[self.product.id]),
            {'quantity': 1, 'size': '41', 'override': False}
        )

        # Submit order form
        response = self.client.post(reverse('orders:order_create'), {
            'first_name': 'Carlos',
            'last_name': 'González',
            'email': 'carlos@example.com',
            'address': 'Av. Libertador 1234',
            'city': 'Santiago',
            'postal_code': '8320000',
            'payment_method': 'credit_card'
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Order.objects.count(), 1)
        order = Order.objects.first()
        self.assertEqual(order.first_name, 'Carlos')
        self.assertEqual(order.get_total_cost(), 240000)
        self.assertEqual(OrderItem.objects.count(), 1)
        item = OrderItem.objects.first()
        self.assertEqual(item.size, '41')
