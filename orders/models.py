from django.db import models
from shop.models import Gabardin


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя*')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия*')
    father_name = models.CharField(max_length=50, verbose_name='Отчество', blank=True)
    number_phone = models.CharField(max_length=20, verbose_name='Телефон*')
    email = models.EmailField(verbose_name='Email*')
    company = models.CharField(max_length=100, verbose_name='Компания', blank=True)
    city = models.CharField(max_length=100, verbose_name='Город*')
    content = models.CharField(max_length=1000, verbose_name='Комментарий', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.pk)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    gabardin = models.ForeignKey(Gabardin, on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.pk)

    def get_cost(self):
        return self.price * self.quantity
