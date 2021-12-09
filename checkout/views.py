from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect(reverse('shop'))
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51K4qV7KgmAoVQepoB33oaZkIRiyGp9n9eHeMTav9zk1Oc8y4Rt2aJ7UBiIU1JZw3HO9fvmYzWppOAHJvvrGwxT4x00fKDPJhhu',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)