from django.db import models
from store.models import Product


PAYMENT_METHOD_CHOICES = [
    ('credit_card', 'Tarjeta de Crédito / Débito'),
    ('webpay', 'Webpay Plus / Transbank'),
    ('bank_transfer', 'Transferencia Bancaria Directa'),
]


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Nombre')
    last_name = models.CharField(max_length=50, verbose_name='Apellido')
    email = models.EmailField(verbose_name='Correo Electrónico')
    address = models.CharField(max_length=250, verbose_name='Dirección de Envío')
    city = models.CharField(max_length=100, verbose_name='Ciudad / Comuna')
    postal_code = models.CharField(max_length=20, verbose_name='Código Postal', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=True, verbose_name='Pagado')
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES,
        default='credit_card',
        verbose_name='Método de Pago'
    )

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'

    def __str__(self):
        return f'Pedido #{self.id} - {self.first_name} {self.last_name}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        related_name='order_items',
        on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=0)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=10, default='40')

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity

