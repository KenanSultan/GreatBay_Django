from django.db import models
from users_app.models import Customer

class Category(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} | {self.owner}"
        
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.price}$ | {self.category}"
