from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from Shoptrade.utility  import *
from rest_framework.decorators import api_view
from .controllers import *
from rest_framework.pagination import PageNumberPagination


# Create your views here.
@api_view(['GET'])
def get_customer_list(request):
    try:
        data = get_customer_list_data(request)
        return Response(data=data, status=status.HTTP_200_OK)
    except Exception as e:
        exception_detail()
        return Response(data={'status': 'error'}, status=status.HTTP_300_MULTIPLE_CHOICES)

# View a list of Customers alongside their aggregated order count
@api_view(['GET'])
def get_customers_order_count(request):
    try:
        data = get_customer_order_count_data(request)
        return Response(data=data, status=status.HTTP_200_OK)
    except Exception as e:
        exception_detail()
        return Response(data={'status': 'error'}, status=status.HTTP_300_MULTIPLE_CHOICES)


# Through post api, we enter customer_name to get the order details of that customer.
@api_view(['POST'])
def get_customer_order_data(request):
    try:
        data = order_data_detail(request)
        return Response(data=data, status=status.HTTP_200_OK)
    except Exception as e:
        exception_detail()
        return Response(data={'status': 'error'}, status=status.HTTP_300_MULTIPLE_CHOICES)


@api_view(['GET'])
def get_order_list(request):
    try:
        data = get_order_list_data(request)
        # pagination_class=PageNumberPagination
        return Response(data=data, status=status.HTTP_200_OK)
    except Exception as e:
        exception_detail()
        return Response(data={'status': 'error'}, status=status.HTTP_300_MULTIPLE_CHOICES)

#Update customer information both in store (through the API) by using a web page.
@api_view(['PUT'])
def update_customer_details(request,pk,format=None):
    try:
        data = update_customer_data(request,pk)
        return Response(data=data, status=status.HTTP_200_OK)
    except Exception as e:
        exception_detail()
        return Response(data={'status': 'error'}, status=status.HTTP_300_MULTIPLE_CHOICES)
