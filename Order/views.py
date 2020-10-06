from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart, Order
from Store.models import Item


# ADD TO CART VIEW
@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Item, pk=pk)
    order_item = Cart.objects.get_or_create(item=item, user=request.user, purchased=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item[0].quantity += 1
            order_item[0].save()
            messages.info(request, "This item quantity has been updated!")
            return redirect('store:home')
        else:
            order.orderitems.add(order_item[0])
            messages.success(request, 'This item has been added to your cart!')
            return redirect('store:home')
    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        messages.success(request, 'This item has been added to your cart!')
        return redirect('store:home')


# CART CIEW
@login_required
def cart(request):
    carts = Cart.objects.filter(user=request.user, purchased=False)
    orders = Order.objects.filter(user=request.user, ordered=False)
    if carts.exists() and orders.exists():
        order = orders[0]
        return render(request, 'Order/cart.html', {'carts': carts, 'order': order})
    else:
        messages.warning(request, "You don't have any item in your cart.")
        return redirect('store:home')