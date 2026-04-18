from django.contrib import admin
from .models import Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'book', 'rating')
    list_select_related = ('client', 'book')


admin.site.register(Review, ReviewAdmin)