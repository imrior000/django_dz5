from django.core.management.base import BaseCommand
from myapp3.models import Order, Client, Product

class Command(BaseCommand):
    help = "Create product."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('tovar', type=str, help='name')
    
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        tovar = kwargs.get('tovar').split(',')
        product = []
        for i in range(len(tovar)):
            temp = Product.objects.filter(pk=tovar[i]).first()
            if not i:
                summ = temp.price
            else:
                summ += temp.price
            product.append(temp)
        order = Order(customer=client, total_price=summ)
        order.save()
        order.products.set(product)
        order.save()
        self.stdout.write(f'{order}')