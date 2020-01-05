from django.db import models

class ProductData(models.Model):
    product_id=models.IntegerField()
    product_name=models.CharField(max_length=50)
    product_cost=models.IntegerField()
    product_class=models.CharField(max_length=50)
    no_of_products=models.CharField(max_length=50)
    manfacture_date=models.DateField(max_length=50)
    expiry_date=models.DateField(max_length=50)
    customer_name=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=50)
