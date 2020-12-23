from .models import *
from .serializers import *
from Shoptrade.utility import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics


# get customer list
def get_customer_list_data(request):
    success_status = 'error'
    msg = 'Error in getting user list'
    data = {}
    try:

        obj = Customer.objects.filter()
        serializer = CustomerListSerializer(obj, many=True)
        data = serializer.data
        success_status = 'success'
        msg = 'Success in getting user list.'
    except Exception as e:
        exception_detail()
    return {'status': success_status, 'msg': msg, 'data': data}


# View a list of Customers alongside their aggregated order count
def get_customer_order_count_data(request):
    success_status = 'error'
    msg = 'Error in getting user list'
    data = {}
    try:
        filter_backends = [filters.SearchFilter]
        search_fields = ['customer_name', 'customer_email']

        order = 0
        customer_orders_list = []

        customer_obj = Customer.objects.filter()
        customer_serializer = CustomerSearchListSerializer(customer_obj, many=True)

        data = customer_serializer.data

        for i in data:
            obj1 = Order.objects.filter(Customer__customer_name__contains=i['customer_name'])
            #print(obj1)
            customer_orders_list.append({'customer_name': i['customer_name'], 'order_count': len(obj1),'customer_email': i['customer_email']})

        success_status = 'success'
        msg = 'Success in getting user list.'
    except Exception as e:
        exception_detail()
    return {'status': success_status, 'msg': msg, 'data': customer_orders_list}


# trigger customer (order ingestion from store)
def order_data_detail(request):
    success_status = 'error'
    msg = 'Error in saving user detail'
    try:
        post_data = request.data
        print(post_data)
        if post_data:
            user_obj = Customer()
            user_obj.customer_name = post_data.get('customer_name')
            obj = Order.objects.filter(Customer__customer_name__contains=user_obj.customer_name)
            serializer = OrderListSerializer(obj, many=True)
            data = serializer.data
            success_status = 'success'
            msg = 'success in saving user detail'
    except Exception as e:
        exception_detail()
    return {'status': success_status, 'msg': msg, 'data': data}


# to get order list
def get_order_list_data(request):
    success_status = 'error'
    msg = 'Error in getting user list'
    data = {}
    try:
        obj = Order.objects.filter()
        serializer = CustomOrderListSerializer(obj, many=True)
        data = serializer.data
        success_status = 'success'
        msg = 'Success in getting user list.'
    except Exception as e:
        exception_detail()
    return {'status': success_status, 'msg': msg, 'data': data}

def update_customer_data(request,pk):
    try:
        print('pk',pk)
        try:
            snippet = Customer.objects.get(pk=pk)
        except Exception as e:
            success_status = 'Error'
            msg = "Entered Customer does'nt exist"
            return {'status': success_status, 'msg': msg}
        #print("snippet is:",snippet)

        serializer = CustomerListSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
        success_status = 'success'
        msg = 'Successfully updated the data'
    except Exception as e:
        exception_detail()
    return {'status': success_status, 'msg': msg}
