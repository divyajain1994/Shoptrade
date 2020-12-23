from rest_framework import serializers
from .models import *


# from datetime import datetime


class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


# View a list of Customers alongside their aggregated order count
class CustomerSearchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_name','customer_email')


# Trigger a customer & order ingestion from the store
class OrderListSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source="Customer.customer_name")

    class Meta:
        model = Order
        fields = ('order_id', 'customer_name', 'product_quantity_details', 'start_date_support', 'end_date_support')


class CustomOrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('order_id', 'product_quantity_details')
