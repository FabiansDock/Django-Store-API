from typing import Collection
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F
from store.models import Customer, Order, OrderItem, Product


def calculate():
    x = 1
    y = 2
    return x


def say_hello(request):
    customer_set = Customer.objects.filter(email__icontains='.com')
    # collection_set = Collection.objects.filter(featured_product__isnull=True)
    product_set = Product.objects.filter(inventory__lt=10)
    order_set = Order.objects.filter(customer__id=1)
    orderitems_set = OrderItem.objects.filter(product__collection__id=3)
    query_set = Product.objects.filter(
        id__in=OrderItem.objects.values_list('id').distinct()).order_by('title')
    return render(request, 'hello.html', {'name': 'Mosh', 'products': orderitems_set})
