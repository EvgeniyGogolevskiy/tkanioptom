from django.shortcuts import render, get_object_or_404

from .models import Gabardin, Category
from basket.forms import BasketAddGabardinForm


def index(request):
    context = {'title': 'Модница текс'}
    return render(request, 'shop/index.html', context=context)


def how_to_buy(request):
    return render(request, 'shop/how_to_buy.html', {'title': 'Как купить'})


def contacts(request):
    return render(request, 'shop/contacts.html', {'title': 'Контакты'})


def basket_empty(request):
    return render(request, 'shop/basket.html', {'title': 'Корзина пуста'})


def warehouse(request):
    category = Category.objects.get(name='габардин на складе')
    gabardin = Gabardin.objects.filter(category=category)
    return render(request, 'shop/warehouse.html', {'title': 'Габардин на складе', 'gabardin': gabardin})


def road(request):
    category = Category.objects.get(name='габардин в пути')
    gabardin = Gabardin.objects.filter(category=category)
    return render(request, 'shop/road.html', {'title': 'Габардин в пути', 'gabardin': gabardin})


def gabardin_detail(request, g_slug):
    gabardin = get_object_or_404(Gabardin, slug=g_slug)
    title = 'Габардин FUHUA'
    basket_gabardin_form = BasketAddGabardinForm()

    return render(request, 'shop/gabardin.html', {'gabardin': gabardin,
                                                  'basket_gabardin_form': basket_gabardin_form,
                                                  'title': title})
