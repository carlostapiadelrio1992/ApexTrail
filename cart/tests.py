from django.test import TestCase
from django.urls import reverse
from store.models import Category, Product
from cart.cart import Cart


class CartTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Entrenamiento', slug='entrenamiento')
        self.product = Product.objects.create(
            category=self.category,
            name='Terrex Soulstride Flow',
            slug='terrex-soulstride-flow',
            description='Entrenamiento runner',
            price=160000,
            sizes=[39, 40, 41],
            available=True
        )

    def test_cart_add_and_remove(self):
        session = self.client.session
        response = self.client.post(
            reverse('cart:cart_add', args=[self.product.id]),
            {'quantity': 2, 'size': '40', 'override': False}
        )
        self.assertEqual(response.status_code, 302)
        
        cart = Cart(response.wsgi_request)
        self.assertEqual(len(cart), 2)
        self.assertEqual(cart.get_total_price(), 320000)

        # Remove item
        response_remove = self.client.post(
            reverse('cart:cart_remove', args=[self.product.id, '40'])
        )
        self.assertEqual(response_remove.status_code, 302)
        cart_after = Cart(response_remove.wsgi_request)
        self.assertEqual(len(cart_after), 0)

    def test_cart_detail_view(self):
        response = self.client.get(reverse('cart:cart_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tu Carrito de Compras')
