from decimal import Decimal
from django.conf import settings
from shop.models import Gabardin


class Basket(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if not basket:
            # save an empty basket in the session
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    def add(self, gabardin, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        gabardin_id = str(gabardin.id)
        if gabardin_id not in self.basket:
            self.basket[gabardin_id] = {'quantity': 0,
                                        'price': str(gabardin.price)}
        if update_quantity:
            self.basket[gabardin_id]['quantity'] = quantity
        else:
            self.basket[gabardin_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Обновление сессии basket
        self.session[settings.BASKET_SESSION_ID] = self.basket
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, gabardin):
        """
        Удаление товара из корзины.
        """
        gabardin_id = str(gabardin.id)
        g_id = gabardin.id
        q = Gabardin.objects.get(id=g_id)
        q.quantity = q.quantity + self.basket[gabardin_id]['quantity']
        q.save()
        if gabardin_id in self.basket:
            del self.basket[gabardin_id]
            self.save()

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        gabardin_ids = self.basket.keys()
        # получение объектов gabardin и добавление их в корзину
        gabardins = Gabardin.objects.filter(id__in=gabardin_ids)
        for gabardin in gabardins:
            self.basket[str(gabardin.id)]['gabardin'] = gabardin

        for item in self.basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(item['quantity'] for item in self.basket.values())

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.basket.values())

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.BASKET_SESSION_ID]
        self.session.modified = True
