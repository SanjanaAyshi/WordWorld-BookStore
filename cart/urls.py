from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShoppingCartViewSet, CartItemViewSet

router = DefaultRouter()
router.register(r'carts', ShoppingCartViewSet)
router.register(r'cart-items', CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]