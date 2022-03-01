from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    help = "This command tells me that he loves me"

    """     def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="How many times do you want me to tell you tha I love"
        )
        """

    def handle(self, *args, **options):
        amenities = [
            "Wifi",
            "Kitchen",
            "Self check_in",
            "Pool",
            "Hot tub",
            "Washing machine",
            "Dryer",
            "Air conditioning",
            "Heating",
            "Dedicated workspace",
            "Indoor fireplace",
            "Gym",
            "Breakfast",
            "Free parking",
            "EV charger",
            "Hair dryer",
            "Iron",
            "High chair",
            "Beachfront",
            "Waterfront",
            "Smoke alarm",
            "Carbon monoxide alarm",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))
