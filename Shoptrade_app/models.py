from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    customer_location = models.CharField(max_length=255)



    def __str__(self):
        return self.customer_name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    product_quantity_details = models.CharField(max_length=255)
    start_date_support = models.DateField(blank=True, null=True)
    end_date_support = models.DateField(blank=True, null=True)
    Customer = models.ForeignKey(Customer,on_delete=models.CASCADE)



    def __str__(self):
        return self.product_quantity_details