from django.shortcuts import render
from django.db.models import Q, F
from django.db.models.aggregates import Count, Max, Min, Avg, Sum

from store.models import Product, Order, Customer


def say_hello(request):
    query_set = []
    product = None
    result = None

    # FILTER
    # query_set = Product.objects.filter(unit_price__range=(20, 30)).all()
    # query_set = Product.objects.filter(collection__id__range=(1, 3)).all()
    # query_set = Product.objects.filter(title__icontains='coffee').all()
    # query_set = Product.objects.filter(last_update__year=2021).all()
    # query_set = Product.objects.filter(description__isnull=True).all()

    # FILTER AND-OR-NOT
    #* Products: inventory < 10 OR price < 20
    # & AND; | OR; ~ NOT
    # query_set = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20)).all()

    # FILTER REFERENCE
    #* Products: inventory = price
    # query_set = Product.objects.filter(inventory=F('unit_price')).all()

    # ORDER BY
    # query_set = Product.objects.order_by('title').all() # ASC
    # query_set = Product.objects.order_by('-title').all() # DESC
    # query_set = Product.objects.order_by('unit_price', '-title').all()

    # FILTER, ACCESS ELEMENT
    # product = Product.objects.order_by('unit_price')[0] # Return a query_set
    # product = Product.objects.earliest('unit_price') # Order by ASC, get first element
    # product = Product.objects.latest('unit_price') # Order by DESC, get first element

    # LIMIT
    # query_set = Product.objects.all()[:5] # LIMIT 5
    # query_set = Product.objects.all()[5:10] # LIMIT 5 OFFSET 5

    # Specific field to query
    # query_set = Product.objects.values('id', 'title', 'collection__title')

    # JOIN
    # select_related (1)
    # query_set = Product.objects.select_related('collection').all()
    # prefetch_related (n)
    # query_set = Product.objects.prefetch_related('promotions').all()
    # Nested JOIN
    # query_set = Product.objects.prefetch_related('promotions').select_related('collection').all()

    # Exercise: Get the last 5 orders with their customer and items (including product)
    # query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # #? Access data after query
    # for query in query_set:
    #     #? Access Order data
    #     print(query.customer.first_name)
    #     for ord_item in query.orderitem_set.all():
    #         #? Access Order Item data
    #         print(ord_item.product.title)

    # AGGRIGATE
    # result = Product.objects.aggregate(count=Count('id'), min_price=Min('unit_price'))
    # result = Product.objects.filter(collection__id=1).aggregate(count=Count('id'), min_price=Min('unit_price'))

    # ANNOTATING
    # query_set = Customer.objects.annotate(is_new=True).all()


    return render(request, 'hello.html', {'name': 'Duy', 'products': list(query_set), 'product': product, 'result': result})