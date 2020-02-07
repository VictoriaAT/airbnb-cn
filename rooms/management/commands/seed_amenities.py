from django.core.management.base import BaseCommand
from rooms.models import Amenity

class Command(BaseCommand):
    help = "This command creates amenities"

    def handle(self, *args, **options):
        amenities = [
            "Air Conditioning",
            "Alarm Clock",
            "Balcony",
            "Bathroom",
            "Bathtub",
            "Bed Linen",
            "Boating",
            "Cable TV",
            "Carbon monoxide detector",
            "Chairs",
            "Children Area",
            "Coffee Maker in Room",
            "Cooking hob",
            "Cookware & Kitchen Utensils",
            "Dishwasher",
            "Double bed",
            "En suite bathroom",
            "Free Parking",
            "Free Wireless Internet",
            "Freezer",
            "Sofa",
            "Stereo",
            "Swimming pool",
            "Toilet",
            "Towels",
            "TV",
        ]

        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))
