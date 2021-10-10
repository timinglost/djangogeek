from django.shortcuts import render
from mainapp.models import ProductsCategory


def products(request):
    title = 'Каталог'

    links_menu = ProductsCategory.objects.all()

    context = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, 'mainapp/products.html', context)

