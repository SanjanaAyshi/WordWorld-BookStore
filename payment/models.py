from django.db import models
from django.core.validators import MinValueValidator
from order.models import Order
# Create your models here.

class Payment(models.Model):
    PAYMENT_METHOD = [
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('net_banking', 'Net Banking'),
        ('bkash', 'Bkash'),
    ]
    
    PAYMENT_STATUS = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]
    order=models.ForeignKey(Order,on_delete=models.PROTECT,related_name='payments')
    payment_date=models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)]
    )
    payment_method=models.CharField(
         max_length=20,
         choices=PAYMENT_METHOD
    )
    payment_status=models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default='pending'
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-payment_date']
        verbose_name='Payment'
        verbose_name_plural="Payments"

    def __str__(self):
        return f"Payment #{self.id} -{self.payment_status}"
