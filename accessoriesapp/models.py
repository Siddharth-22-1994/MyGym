from django.db import models
status = [('Available', 'Available'), ('Sold Out', 'Sold Out')]
catagory = [('Dumbles', 'Dumbles'), ('Trademill', 'Trademill'), ('Elliptical Trainer', 'Elliptical Trainer'), ('Bikes', 'Bikes'), ('Rowers', 'Rowers')]


# Create your models here.

class prodmodel(models.Model):
    Name = models.CharField(max_length=50)
    Prod_id = models.CharField(max_length=20)
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    Specification = models.CharField(max_length=200)
    Status = models.CharField(max_length=20, choices=status, default='Available')
    Pictures = models.FileField(upload_to='pictures', null=True, blank=True)
    Eqipment = models.CharField(max_length=20, choices=catagory, default='Available', null=True, blank=True)