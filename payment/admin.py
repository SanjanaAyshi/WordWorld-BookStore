from django.contrib import admin
from .models import Payment
# Register your models here.

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'payment_date', 'payment_status')
    list_select_related = ('order',)

admin.site.register(Payment,PaymentAdmin)
