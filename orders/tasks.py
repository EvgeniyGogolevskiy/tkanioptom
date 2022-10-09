from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Заказ №{order_id} оформлен'
    message = f'Уважаемый(ая) {order.first_name} Ваш заказ № {order_id} успешно оформлен!\n' \
              f'Ожидайте подтверждения по телефону.'
    mail_sent = send_mail(subject, message, 'evgeni3197@gmail.com', [order.email], fail_silently=False)
    print('OK ', order_id)
    return mail_sent


@shared_task
def order_push(order_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Некий {order.first_name} оформил заказ №{order_id}'
    message = f'Заказ № {order_id} оформлен!\n ФИО клиента {order.last_name} {order.first_name} {order.father_name}\n' \
              f'Емэйл {order.email}\n Телефон {order.number_phone}'
    mail_sent = send_mail(subject, message, 'evgeni3197@gmail.com', ['evgeni3197@mail.ru'], fail_silently=False)
    print('OK2 ', order_id)
    return mail_sent

#celery -A tkanioptom worker -l INFO

