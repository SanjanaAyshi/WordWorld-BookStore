from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'order_date', 'status')
    list_select_related = ('client',)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'book', 'quantity', 'price')
    list_select_related = ('order', 'book')

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)