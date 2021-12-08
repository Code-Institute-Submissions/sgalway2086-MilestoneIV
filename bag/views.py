from django.shortcuts import render, redirect


def view_bag(request):
    return render(request, 'bag/shopping-bag.html')


def add_to_bag(request, item_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})
    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)

def remove_from_bag(request, item_id):

    print('REACHED function')
    print(item_id)
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    if item_id in list(bag.keys()):
        print('REACHED REMOVE')
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(redirect_url)