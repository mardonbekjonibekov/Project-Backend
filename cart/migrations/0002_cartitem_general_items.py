from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0001_initial"),
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(name="cartitem", unique_together=set()),
        migrations.AddField(
            model_name="cartitem",
            name="item_name",
            field=models.CharField(blank=True, max_length=180),
        ),
        migrations.AddField(
            model_name="cartitem",
            name="item_type",
            field=models.CharField(
                choices=[
                    ("event", "Event"),
                    ("gift_certificate", "Gift Certificate"),
                    ("monthly_giving", "Monthly Giving"),
                    ("donation", "Donation"),
                ],
                default="event",
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name="cartitem",
            name="event",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cart_items",
                to="events.event",
            ),
        ),
    ]
