from django.shortcuts import get_object_or_404, render
from .models import Product
from cart.cart import Cart


def product_list(request, category_slug=None):
    cart = Cart(request)
    products = Product.objects.filter(available=True)
    return render(request, 'list.html', {'products': products, 'cart': cart})


def product_detail(request, id, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request,
                  'product_detail.html',
                  {'product': product, 'cart': cart}
                  )
