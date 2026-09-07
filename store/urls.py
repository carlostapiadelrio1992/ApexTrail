from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'store'

router = DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='api-category')
router.register('products', views.ProductViewSet, basename='api-product')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
