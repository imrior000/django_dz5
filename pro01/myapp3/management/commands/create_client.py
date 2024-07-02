from django.core.management.base import BaseCommand
from myapp3.models import Client

class Command(BaseCommand):
    help = "Create client."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='name')
        parser.add_argument('email', type=str, help='email')
        parser.add_argument('phone', type=int, help='phone')
        parser.add_argument('address', type=str, help='address')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone = kwargs.get('phone')
        address = kwargs.get('address')
        client = Client(name=name, email=email, phone=phone, addres=address)
        client.save()
        self.stdout.write(f'{client}')