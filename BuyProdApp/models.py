from django.db import models
from datetime import datetime
from datetime import datetime


# Create your models here.
class BuyProductModel(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)
    Product = models.CharField(max_length=100)
    Prod_id = models.CharField(max_length=100)
    Quantity = models.IntegerField()
    card_number = models.CharField(max_length=100)
    Name_on_card = models.CharField(max_length=100)
    cvv = models.IntegerField()
    Date = models.DateTimeField(default=datetime.now(), blank=True)
