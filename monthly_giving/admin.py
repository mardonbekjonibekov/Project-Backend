from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import MonthlyGivingOption


@admin.register(MonthlyGivingOption)
class MonthlyGivingOptionAdmin(ModelAdmin):
    list_display = ("title", "amount", "is_featured", "is_active", "display_order")
    list_editable = ("amount", "is_featured", "is_active", "display_order")
    list_filter = ("is_featured", "is_active")
    search_fields = ("title", "description")
    ordering = ("display_order", "amount")
