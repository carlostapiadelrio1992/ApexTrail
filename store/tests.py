from django.test import TestCase
from django.urls import reverse
from django.core.management import call_command
from store.models import Category, Product


class StoreModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Competición', slug='competicion')
        self.product = Product.objects.create(
            category=self.category,
            name='Terrex Agravic Speed Ultra',
            slug='terrex-agravic-speed-ultra',
            description='Test description',
            price=220000,
            sizes=[38, 39, 40, 41],
            available=True
        )

    def test_category_str_and_url(self):
        self.assertEqual(str(self.category), 'Competición')
        self.assertEqual(self.category.get_absolute_url(), reverse('store:product_list_by_category', args=['competicion']))

    def test_product_str_and_url(self):
        self.assertEqual(str(self.product), 'Terrex Agravic Speed Ultra')
        self.assertEqual(self.product.get_absolute_url(), reverse('store:product_detail', args=[self.product.id, self.product.slug]))

    def test_product_list_view(self):
        response = self.client.get(reverse('store:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Terrex Agravic Speed Ultra')

    def test_product_detail_view(self):
        response = self.client.get(self.product.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test description')

    def test_seed_products_command(self):
        call_command('seed_products')
        self.assertGreater(Product.objects.count(), 1)
