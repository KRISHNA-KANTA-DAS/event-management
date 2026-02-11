from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import Order
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('cart')


@login_required
def cart_view(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0

    for pid, qty in cart.items():
        product = Product.objects.get(id=pid)
        product.quantity = qty
        product.subtotal = product.price * qty
        total += product.subtotal
        products.append(product)

    return render(request, 'cart.html', {'products': products, 'total': total})


@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    for pid, qty in cart.items():
        product = Product.objects.get(id=pid)
        Order.objects.create(
            user=request.user,
            product=product,
            quantity=qty
        )
    request.session['cart'] = {}
    return render(request, 'success.html')
