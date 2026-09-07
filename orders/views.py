from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cart.cart import Cart
from store.models import Product
from .models import OrderItem, Order
from .forms import OrderCreateForm


def order_create(request):
    cart = Cart(request)
    if len(cart) == 0:
        return redirect('store:product_list')

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.paid = True
            order.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                    size=item['size']
                )

            cart.clear()
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()

    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})


@api_view(['POST'])
def order_api_create(request):
    data = request.data
    first_name = data.get('first_name', '')
    last_name = data.get('last_name', '')
    email = data.get('email', '')
    address = data.get('address', '')
    city = data.get('city', '')
    postal_code = data.get('postal_code', '')
    payment_method = data.get('payment_method', 'credit_card')
    items_data = data.get('items', [])

    if not items_data:
        return Response({'error': 'El pedido no contiene productos.'}, status=400)

    order = Order.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        address=address,
        city=city,
        postal_code=postal_code,
        payment_method=payment_method,
        paid=True
    )

    created_items = []
    for item in items_data:
        product_id = item.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        quantity = int(item.get('quantity', 1))
        size = str(item.get('size', '40'))

        order_item = OrderItem.objects.create(
            order=order,
            product=product,
            price=product.price,
            quantity=quantity,
            size=size
        )
        created_items.append({
            'product': product.name,
            'quantity': quantity,
            'size': size,
            'price': float(product.price)
        })

    return Response({
        'status': 'success',
        'order_id': order.id,
        'total_cost': float(order.get_total_cost()),
        'items': created_items,
        'message': 'Pedido creado con éxito.'
    })
