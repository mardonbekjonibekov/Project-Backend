from datetime import date
from decimal import Decimal

from django.core.management.base import BaseCommand

from donations.models import DonationOption
from events.models import Event
from gift_certificates.models import GiftCertificateOrder
from monthly_giving.models import MonthlyGivingOption


class Command(BaseCommand):
    help = "Seed demo content for the Lookingglass purchase clone."

    def handle(self, *args, **options):
        Event.objects.update_or_create(
            title="Untitled Vampire Play",
            defaults={
                "starts_at": date(2026, 6, 4),
                "ends_at": date(2026, 7, 12),
                "short_description": "Think you've got baggage? Try dating when you have centuries of dating history and a literal body count.",
                "long_description": "A darkly funny theatrical event about romance, history, secrets, and the people who try to survive all three.",
                "price": Decimal("58.00"),
                "visual_style": "vampire",
                "display_order": 1,
                "is_active": True,
            },
        )
        Event.objects.update_or_create(
            title="LookingGlass: Stage Combat 101",
            defaults={
                "starts_at": date(2026, 6, 17),
                "ends_at": date(2026, 7, 11),
                "short_description": "Have you ever wanted to safely punch someone in the face? Go behind the scenes of every production.",
                "long_description": "A hands-on workshop introducing the fundamentals of stage combat, safety, rhythm, and theatrical storytelling.",
                "price": Decimal("45.00"),
                "visual_style": "workshop",
                "display_order": 2,
                "is_active": True,
            },
        )

        for order, amount in enumerate((25, 50, 100, 250), start=1):
            GiftCertificateOrder.objects.update_or_create(
                name=f"${amount} Gift Certificate",
                defaults={
                    "amount": Decimal(amount),
                    "description": "Give someone a flexible theatre experience they can use toward tickets.",
                    "display_order": order,
                    "is_active": True,
                },
            )

        for order, amount in enumerate((10, 25, 50, 100), start=1):
            MonthlyGivingOption.objects.update_or_create(
                title=f"${amount} Monthly Supporter",
                defaults={
                    "amount": Decimal(amount),
                    "description": "Sustain new work, workshops, and accessible theatre programs every month.",
                    "display_order": order,
                    "is_featured": amount == 50,
                    "is_active": True,
                },
            )

        for order, amount in enumerate((25, 75, 150, 500), start=1):
            DonationOption.objects.update_or_create(
                title=f"Donate ${amount}",
                defaults={
                    "amount": Decimal(amount),
                    "description": "Support bold theatre, artist development, and community programs.",
                    "display_order": order,
                    "is_active": True,
                },
            )

        self.stdout.write(self.style.SUCCESS("Demo content seeded."))
