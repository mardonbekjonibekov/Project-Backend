from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import CartItem


@admin.register(CartItem)
class CartItemAdmin(ModelAdmin):
    list_display = ("label", "item_type", "quantity", "unit_price", "session_key", "created_at")
    list_filter = ("item_type", "created_at", "event")
    search_fields = ("item_name", "event__title", "session_key")
    readonly_fields = ("created_at", "updated_at")
    autocomplete_fields = ("event",)
