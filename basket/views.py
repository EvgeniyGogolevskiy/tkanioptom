from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Gabardin
from .basket import Basket
from .forms import BasketAddGabardinForm
from django.forms.utils import ErrorList


@require_POST
def basket_add(request, gabardin_id):
    basket = Basket(request)
    title = 'Добавление в корзину'
    gabardin = get_object_or_404(Gabardin, id=gabardin_id)
    form = BasketAddGabardinForm(request.POST)
    if int(request.POST.get('quantity')) > gabardin.quantity:
        form.add_error('quantity', 'Введите число, не превышающее наличие!')
        return render(request, 'shop/gabardin.html', {'gabardin': gabardin,
                                                  'basket_gabardin_form': form,
                                                  'title': title})
    if form.is_valid():
        cd = form.cleaned_data
        basket.add(gabardin=gabardin,
                   quantity=cd['quantity'],
                   update_quantity=cd['update'])
    gabardin.quantity = gabardin.quantity - int(request.POST.get('quantity'))
    gabardin.save()
    return redirect('basket_detail')


def basket_remove(request, gabardin_id):
    basket = Basket(request)
    gabardin = get_object_or_404(Gabardin, id=gabardin_id)
    basket.remove(gabardin)
    return redirect('basket_detail')


def basket_detail(request):
    basket = Basket(request)
    title = 'Корзина'
    return render(request, 'basket/detail.html', {'title': title, 'basket': basket})
