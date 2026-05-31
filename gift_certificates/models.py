from django.db import models

class GiftCertificateOrder(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_to_send = models.DateField()
    to_name = models.CharField(max_length=255)  # Mana shu yerda max_length bo'ldi
    send_to_type = models.CharField(max_length=50, default="recipient")  # Bu yerda ham
    recipient_email = models.EmailField(blank=True, null=True)
    from_name = models.CharField(max_length=255)  # Bu yerda ham
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"${self.amount} from {self.from_name} to {self.to_name}"