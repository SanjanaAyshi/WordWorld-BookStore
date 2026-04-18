from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from client.models import Client
from catalog.models import Book


class Review(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['client', 'book']
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.client.name} - {self.book.title} ({self.rating}⭐)"