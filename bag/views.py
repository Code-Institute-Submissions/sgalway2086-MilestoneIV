from django.shortcuts import render, redirect
from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg


def view_bag(request):
    return render(request, 'bag/shopping-bag.html')


def add_to_bag(request, item_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
    request.session['bag'] = bag
    return redirect(redirect_url)

