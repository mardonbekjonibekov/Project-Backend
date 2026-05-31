from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import DonationOption


@admin.register(DonationOption)
class DonationOptionAdmin(ModelAdmin):
    list_display = ("title", "amount", "is_active", "display_order")
    list_editable = ("amount", "is_active", "display_order")
    list_filter = ("is_active",)
    search_fields = ("title", "description")
    ordering = ("display_order", "amount")
