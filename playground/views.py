from django.shortcuts import render
from store.models import Product


def say_hello(request):
    query_set = Product.objects.filter(unit_price__range=(20, 30)).all()
    # query_set = Product.objects.filter(collection__id__range=(1, 3)).all()
    # query_set = Product.objects.filter(title__icontains='coffee').all()
    # query_set = Product.objects.filter(last_update__year=2021).all()
    # query_set = Product.objects.filter(description__isnull=True).all()

    return render(request, 'hello.html', {'name': 'Duy', 'products': list(query_set)})