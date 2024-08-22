from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from cakeapp.models import Cake, CartItem


@login_required(login_url='login_view')
def user_page(request):
    return render(request, 'user_temp/home.html')


@login_required(login_url='login_view')
def user_cake_view(request):
    cakes = Cake.objects.all()
    return render(request,'user_temp/view_cake.html', {'form': cakes})


def add_to_cart(request, product_id):
    product = Cake.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(cake=product,user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')


def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.cake.price * item.quantity for item in cart_items)
    return render(request, 'user_temp/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')