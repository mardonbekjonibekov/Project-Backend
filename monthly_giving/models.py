from django.db import models


class MonthlyGivingOption(models.Model):
    title = models.CharField(max_length=140)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "amount"]

    def __str__(self):
        return f"{self.title} (${self.amount}/mo)"
