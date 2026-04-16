from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.
class orderAdmin(admin.ModelAdmin):
    list_display=('id', 'client', 'order_date', 'status','total_amount', 'shipping_address')

class OrderItemAdmin(admin.ModelAdmin):
    list_display=('id', "client", 'order_date','status',' total_amount')

admin.site.register(Order,orderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)