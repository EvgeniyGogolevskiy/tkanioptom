from django.shortcuts import render

from .models import OrderItem
from .forms import OrderCreateForm
from basket.basket import Basket
from .tasks import order_created, order_push


def order_create(request):
    basket = Basket(request)
    title = 'Оформление заказа'
    title1 = 'Спасибо за заказ!'
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in basket:
                OrderItem.objects.create(order=order,
                                         gabardin=item['gabardin'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            # очистка корзины
            basket.clear()
            order_created.delay(order.id)
            order_push.delay(order.id)
            return render(request, 'orders/created.html', {'order': order, 'title': title1})
    else:
        form = OrderCreateForm
    return render(request, 'orders/create.html', {'basket': basket, 'form': form, 'title': title})
