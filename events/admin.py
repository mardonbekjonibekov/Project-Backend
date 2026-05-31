from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Event


@admin.register(Event)
class EventAdmin(ModelAdmin):
    list_display = ("title", "starts_at", "ends_at", "price", "is_active", "display_order")
    list_editable = ("price", "is_active", "display_order")
    list_filter = ("is_active", "visual_style", "starts_at")
    search_fields = ("title", "short_description", "long_description")
    ordering = ("display_order", "starts_at")
    readonly_fields = ("created_at", "updated_at")
    list_per_page = 25
    actions = ("mark_active", "mark_inactive")
    fieldsets = (
        ("Public card", {"fields": ("title", "short_description", "long_description")}),
        ("Schedule and sales", {"fields": ("starts_at", "ends_at", "price", "button_label")}),
        ("Visuals", {"fields": ("image", "visual_style")}),
        ("Owner controls", {"fields": ("is_active", "display_order")}),
        ("Audit", {"classes": ("collapse",), "fields": ("created_at", "updated_at")}),
    )

    @admin.action(description="Make selected events visible")
    def mark_active(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description="Hide selected events")
    def mark_inactive(self, request, queryset):
        queryset.update(is_active=False)
