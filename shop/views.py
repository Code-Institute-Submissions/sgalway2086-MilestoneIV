from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def shop(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'shop/shop.html', context)


def view_product(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'shop/view_product.html', context)
