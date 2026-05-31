from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import GiftCertificateOrder

@admin.register(GiftCertificateOrder)
class GiftCertificateOrderAdmin(ModelAdmin):
    list_display = ("id", "amount", "from_name", "to_name", "created_at")
    list_filter = ("created_at", "send_to_type")
    search_fields = ("from_name", "to_name", "recipient_email")