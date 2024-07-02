from django.core.management.base import BaseCommand
from myapp3.models import Product

class Command(BaseCommand):
    help = "Create product."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='name')
        parser.add_argument('description', type=str, help='description')
        parser.add_argument('price', type=int, help='price')
        parser.add_argument('col', type=int, help='col')
    
    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        description = kwargs.get('description')
        price = kwargs.get('price')
        col = kwargs.get('col')
        product = Product(name=name, description=description, price=price, col=col)
        product.save()
        self.stdout.write(f'{product}')