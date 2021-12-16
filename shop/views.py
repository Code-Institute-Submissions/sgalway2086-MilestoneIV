from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category, Review
from .forms import ProductForm


def shop(request):

    products = Product.objects.all()
    query = None
    category = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)



        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, "Please search a valid query to search the store")
                return redirect(reverse('shop'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting
    }

    return render(request, 'shop/shop.html', context)

def view_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.all()

    context = {
        'product': product,
        'reviews': reviews,
    }

    return render(request, 'shop/view_product.html', context)

@login_required
def add_product(request):
    if not request.user.is_superuser:
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product')
            return redirect(reverse('view_product', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please check the form')
    else:
        form = ProductForm()

    template = 'shop/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    if not request.user.is_superuser:
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product')
            return redirect(reverse('view_product', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please check the form is valid')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'shop/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted')
    return redirect(reverse('shop'))


def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        review_count = product.review_quantity
        if product.rating:
            average_rating = product.rating
        else:
            average_rating = 0
        rating = review_count * average_rating
        new_rating = rating + int(request.POST.get('rating-number'))
        new_rating = new_rating / (review_count + 1)
        product.review_quantity += 1
        product.rating = new_rating
        product.save()
        messages.success(request, 'Successfully rated product')
        return redirect(reverse('view_product', args=[product.id]))
    else:
        return redirect(reverse('view_product', args=[product.id]))


def add_text_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        if request.user.is_authenticated:
            review = Review()
            review.review_for_product_id = product_id
            review.user = request.user
            review.review_text = request.POST.get('r_text')
            review.rating = int(request.POST.get('rating'))
            review.title = request.POST.get('title')
            review_count = product.review_quantity

            if product.rating:
                average_rating = product.rating
            else:
                average_rating = 0
            rating = review_count * average_rating
            new_rating = rating + int(request.POST.get('rating'))
            new_rating = new_rating / (review_count + 1)
            product.review_quantity += 1
            product.rating = new_rating
            product.save()
            review.save()
            return redirect(reverse('view_product', args=[product.id]))
        else:
            messages.error(request, 'Can not submit review. Please Log in')
            return redirect(reverse('view_product', args=[product.id]))
