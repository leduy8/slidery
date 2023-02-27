from django.shortcuts import render
from django.db.models import Q, F, Value, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.contrib.contenttypes.models import ContentType

from store.models import Product, Order, Customer, Collection
from tags.models import TaggedItem


# def say_hello(request):
#     queryset = []
#     product = None
#     result = None

#     # FILTER
#     # queryset = Product.objects.filter(unit_price__range=(20, 30)).all()
#     # queryset = Product.objects.filter(collection__id__range=(1, 3)).all()
#     # queryset = Product.objects.filter(title__icontains='coffee').all()
#     # queryset = Product.objects.filter(last_update__year=2021).all()
#     # queryset = Product.objects.filter(description__isnull=True).all()

#     # FILTER AND-OR-NOT
#     #* Products: inventory < 10 OR price < 20
#     # & AND; | OR; ~ NOT
#     # queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20)).all()

#     # FILTER REFERENCE
#     #* Products: inventory = price
#     # queryset = Product.objects.filter(inventory=F('unit_price')).all()

#     # ORDER BY
#     # queryset = Product.objects.order_by('title').all() # ASC
#     # queryset = Product.objects.order_by('-title').all() # DESC
#     # queryset = Product.objects.order_by('unit_price', '-title').all()

#     # FILTER, ACCESS ELEMENT
#     # product = Product.objects.order_by('unit_price')[0] # Return a queryset
#     # product = Product.objects.earliest('unit_price') # Order by ASC, get first element
#     # product = Product.objects.latest('unit_price') # Order by DESC, get first element

#     # LIMIT
#     # queryset = Product.objects.all()[:5] # LIMIT 5
#     # queryset = Product.objects.all()[5:10] # LIMIT 5 OFFSET 5

#     # Specific field to query
#     # queryset = Product.objects.values('id', 'title', 'collection__title')

#     # JOIN
#     # select_related (1)
#     # queryset = Product.objects.select_related('collection').all()
#     # prefetch_related (n)
#     # queryset = Product.objects.prefetch_related('promotions').all()
#     # Nested JOIN
#     # queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()

#     # Exercise: Get the last 5 orders with their customer and items (including product)
#     # queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
#     # #? Access data after query
#     # for query in queryset:
#     #     #? Access Order data
#     #     print(query.customer.first_name)
#     #     for ord_item in query.orderitem_set.all():
#     #         #? Access Order Item data
#     #         print(ord_item.product.title)

#     # AGGRIGATE
#     # result = Product.objects.aggregate(count=Count('id'), min_price=Min('unit_price'))
#     # result = Product.objects.filter(collection__id=1).aggregate(count=Count('id'), min_price=Min('unit_price'))

#     # ANNOTATING
#     # queryset = Customer.objects.annotate(is_new=True).all()

#     # EXPRESSION WRAPPER
#     # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
#     # queryset = Product.objects.annotate(
#     #     discounted_price=discounted_price
#     # )

#     return render(request, 'hello.html', {'name': 'Duy', 'products': list(queryset), 'product': product, 'result': result})


def say_hello(request):
    queryset = []
    product = None
    result = None

    # queryset = TaggedItem.objects.get_tags_for(Product, 1)

    # CREATE NEW
    # 1st way
    # collection = Collection()
    # collection.title = 'Video Games'
    # collection.featured_product = Product(pk=1)
    # collection.save()

    # 2nd way
    # collection = Collection()
    # collection.title = 'Video Games'
    # collection.featured_product_id = 1
    # collection.save()

    # 3rd way
    # collection = Collection.objects.create(
    #     title = 'Video Games',
    #     featured_product_id = 1,
    # )

    # UPDATE
    # collection = Collection.objects.filter(pk=11).update(featured_product=None)

    # DELETE
    # DELETE 1
    # collection = Collection.objects.filter(pk=11).delete()
    # DELETE multiple
    # collection = Collection.objects.filter(id__gt=10).delete()

    return render(request, 'hello.html', {'name': 'Duy', 'products': list(queryset), 'product': product, 'result': result})
