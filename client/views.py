from django.shortcuts import render
from rest_framework import viewsets
from .models import Client
from .serializers import clientSerializer
# Create your views here.

class ClientViewSet(viewsets.ModelViewSet):
    queryset=Client.objects.all()
    serializer_class=clientSerializer
