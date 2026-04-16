from django.db import models
from django.core.validators import MinValueValidator
from client.models import Client
from catalog.models import Book


class ShoppingCart(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='carts'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Shopping Cart'
        verbose_name_plural = 'Shopping Carts'
    
    def __str__(self):
        return f"{self.client}'s Cart"


class CartItem(models.Model):
    cart = models.ForeignKey(
        ShoppingCart,
        on_delete=models.CASCADE,
        related_name='items'
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='cart_items'
    )
    quantity = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['cart', 'book']
        ordering = ['cart', 'book']
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'
    
    def __str__(self):
        return f"{self.book.title} x {self.quantity}"