from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from store.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST, product=product)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            size=cd['size'],
            override_quantity=cd['override']
        )
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id, size):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product.id, size)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            product=item['product'],
            initial={
                'quantity': item['quantity'],
                'size': item['size'],
                'override': True,
            }
        )
    return render(request, 'cart/detail.html', {'cart': cart})


# API Endpoints
@api_view(['GET'])
def cart_api_detail(request):
    cart = Cart(request)
    items = []
    for item in cart:
        items.append({
            'product_id': item['product'].id,
            'name': item['product'].name,
            'price': float(item['price']),
            'quantity': item['quantity'],
            'size': item['size'],
            'total_price': float(item['total_price']),
            'image_url': item['product'].image.url if item['product'].image else ''
        })
    return Response({
        'items': items,
        'total_items': len(cart),
        'total_price': float(cart.get_total_price())
    })


@api_view(['POST'])
def cart_api_add(request):
    product_id = request.data.get('product_id')
    quantity = int(request.data.get('quantity', 1))
    size = str(request.data.get('size', '40'))
    override = bool(request.data.get('override', False))

    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.add(product=product, quantity=quantity, size=size, override_quantity=override)
    
    return Response({
        'status': 'success',
        'message': f'{product.name} agregado al carrito.',
        'total_items': len(cart),
        'total_price': float(cart.get_total_price())
    })


@api_view(['POST'])
def cart_api_remove(request):
    product_id = request.data.get('product_id')
    size = str(request.data.get('size', '40'))
    cart = Cart(request)
    cart.remove(product_id=product_id, size=size)
    
    return Response({
        'status': 'success',
        'message': 'Producto removido del carrito.',
        'total_items': len(cart),
        'total_price': float(cart.get_total_price())
    })
