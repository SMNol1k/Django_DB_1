from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('phones.csv', 'r') as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                phone, created = Phone.objects.get_or_create(
                    name=row['name'],
                    price=row['price'],
                    image=row['image'],
                    release_date=row['release_date'],
                    lte_exists=row['lte_exists'],
                    slug=slugify(row['name'], allow_unicode=True)
                )
                if created:
                    print(f"Phone {phone.name} created")
                else:
                    print(f"Phone {phone.name} already exists")