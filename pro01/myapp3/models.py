from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    addres = models.CharField(max_length=255)
    date_register = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Username: {self.name}, email: {self.email}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    col = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to ='media/', default="default.jpg")

    def __str__(self) -> str:
        return f'Product: {self.name}, price: {self.price}, col: {self.col}'

class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Customer: {self.customer}, summ: {self.total_price}'
