from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('customer-list/', get_customer_list),

    # url for View a list of Customers alongside their aggregated order count
    path('customer-order-count-list/', get_customers_order_count),

    # Urls for Trigger a customer & order ingestion from the store
    path('customer-order-details/', get_customer_order_data),

    #View a list of orders over a certain threshold
    path('order-list/', get_order_list),

    #Update customer information both in store (through the API) by using a web page.
    url('update-customer-list/(?P<pk>[0-9]+)$', update_customer_details),
]
