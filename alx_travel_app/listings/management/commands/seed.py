# listings/
#  └─ management/
#      └─ commands/
#          └─ __init__.py
#          └─ seed.py

from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        sample_data = [
            {
                "title": "Beachfront Villa",
                "description": "A beautiful villa by the beach.",
                "price_per_night": 150.00,
                "location": "Mombasa, Kenya",
                "max_guests": 6
            },
            {
                "title": "Mountain Cabin",
                "description": "Cozy cabin with a stunning mountain view.",
                "price_per_night": 120.00,
                "location": "Mt. Kenya, Kenya",
                "max_guests": 4
            },
            {
                "title": "City Apartment",
                "description": "Modern apartment in the heart of the city.",
                "price_per_night": 90.00,
                "location": "Nairobi, Kenya",
                "max_guests": 3
            },
        ]

        for item in sample_data:
            Listing.objects.get_or_create(**item)

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))

