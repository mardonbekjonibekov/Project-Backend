from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=180)),
                ("starts_at", models.DateField()),
                ("ends_at", models.DateField()),
                ("short_description", models.TextField()),
                ("long_description", models.TextField(blank=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                ("image", models.ImageField(blank=True, upload_to="events/")),
                ("visual_style", models.CharField(choices=[("vampire", "Vampire artwork"), ("workshop", "Workshop artwork")], default="vampire", max_length=40)),
                ("button_label", models.CharField(default="Book Now", max_length=40)),
                ("is_active", models.BooleanField(default=True)),
                ("display_order", models.PositiveIntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["display_order", "starts_at", "title"]},
        ),
    ]
