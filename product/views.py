from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.models import CartItem, Cart
from product.models import Product_gallery
from cart.views import cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q


def products(request, category_slug=None):
    """ A view to return the products page and filter by category """
    categories = None
    products = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=categories, is_available=True
            )
        paginator = Paginator(products, 12)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(
            is_available=True).order_by('id')
        paginator = Paginator(products, 12)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count,

    }

    return render(request, "products/products.html", context)


def product_detail(request, category_slug, product_slug):
    """ A view to return the product detail page for a specific product"""

    try:
        single_product = Product.objects.get(
            category__slug=category_slug, slug=product_slug
            )

    except Exception as e:
        raise e

    product_gallery = Product_gallery.objects.filter(
        product_id=single_product.id
        )

    context = {
        'single_product': single_product,
        'product_gallery': product_gallery,
    }

    return render(request, "products/product_detail.html", context)


def search(request):
    """ A view to return the search results page """

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by(
                '-created_date').filter(
                Q(
                    description__icontains=keyword
                    ) | Q(product_name__icontains=keyword)
                    )
            product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }

    return render(request, "products/products.html", context)
