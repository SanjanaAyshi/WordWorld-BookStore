from django.shortcuts import render
from rest_framework import viewsets
from .models import ShoppingCart, CartItem
from .serializers import ShoppingCartSerializer, CartItemSerializer

# Create your views here.
class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer