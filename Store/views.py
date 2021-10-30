from django.shortcuts import render, HttpResponseRedirect
from .models import EBook, Cart_Items
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def storeView(request):
    ebooks = {
        'eBooks': EBook.objects.all()
    }
    return render(request, 'store/index.html', ebooks)


def cartView(request):
    CART_ITEMS = Cart_Items.objects.all()
    cart_total = 0
    for item in CART_ITEMS:
        cart_total += item.price
    return render(request, 'store/cart.html', {
        'cart_items': CART_ITEMS,'cart_total': cart_total
    })

@csrf_exempt
def del_cart_items(request):
    item_id = request.POST['item_id']
    Cart_Items.objects.get(pk=item_id).delete()
    return HttpResponseRedirect('http://127.0.0.1:8000/store/cart')


@csrf_exempt
def add_cart_items(request):
    book_id = request.POST['book_id']
    title = EBook.objects.get(pk =  book_id).title
    price = EBook.objects.get(pk = book_id).price
    item = Cart_Items.objects.create(title = title, price = price)
    return HttpResponseRedirect('http://127.0.0.1:8000/store')
