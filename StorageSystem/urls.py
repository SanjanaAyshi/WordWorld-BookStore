from django.contrib import admin
from django.urls import path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_root(request):
    return Response({
        'clients': request.build_absolute_uri('/api/clients/'),
        'categories': request.build_absolute_uri('/api/catalog/categories/'),
        'publications': request.build_absolute_uri('/api/catalog/publications/'),
        'authors': request.build_absolute_uri('/api/catalog/authors/'),
        'books': request.build_absolute_uri('/api/catalog/books/'),
        'carts': request.build_absolute_uri('/api/cart/carts/'),
        'cart-items': request.build_absolute_uri('/api/cart/cart-items/'),
        'orders': request.build_absolute_uri('/api/order/orders/'),
        'order-items': request.build_absolute_uri('/api/order/order-items/'),
        'payments': request.build_absolute_uri('/api/payment/payments/'),
        'reviews': request.build_absolute_uri('/api/reviews/reviews/'),
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/clients/', include('client.urls')),
    path('api/catalog/', include('catalog.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/order/', include('order.urls')),
    path('api/payment/', include('payment.urls')),
    path('api/reviews/', include('reviews.urls')),
]