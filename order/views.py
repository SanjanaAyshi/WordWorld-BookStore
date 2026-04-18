from django.shortcuts import render
from rest_framework import viewsets
from .models import Order, OrderItem
from .serializers import OrderItemSerializer,OrderSerializer

# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class= OrderItemSerializer