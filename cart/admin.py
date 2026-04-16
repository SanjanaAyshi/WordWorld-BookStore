from django.contrib import admin
from .models import ShoppingCart,CartItem

#class for looks
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display=('id', 'client', 'created_at')

class CartItemAdmin(admin.ModelAdmin):
    list_display=('id', 'cart', 'book', 'quantity')

# Register your models here.
admin.site.register(ShoppingCart,ShoppingCartAdmin)
admin.site.register(CartItem,CartItemAdmin)