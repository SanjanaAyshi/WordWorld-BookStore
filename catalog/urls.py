from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, PublicationViewSet, AuthorViewSet, BookViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'publications', PublicationViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]