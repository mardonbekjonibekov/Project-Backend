from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=180)
    starts_at = models.DateField()
    ends_at = models.DateField()
    short_description = models.TextField()
    long_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="events/", blank=True)
    visual_style = models.CharField(
        max_length=40,
        choices=[("vampire", "Vampire artwork"), ("workshop", "Workshop artwork")],
        default="vampire",
    )
    button_label = models.CharField(max_length=40, default="Book Now")
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order", "starts_at", "title"]

    def __str__(self):
        return self.title
