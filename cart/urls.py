from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/<path:size>/', views.cart_remove, name='cart_remove'),

    
    # API endpoints
    path('api/', views.cart_api_detail, name='cart_api_detail'),
    path('api/add/', views.cart_api_add, name='cart_api_add'),
    path('api/remove/', views.cart_api_remove, name='cart_api_remove'),
]
