# tkanioptom
# Интернет магазин

Интернет-магазин c  каталогом товаров, корзиной и возможностью оформления заказов. 

### Основной функционал:
- каталог товаров пополняемый через админку;
- корзина реализована с помощью `сессий Django`;
- после создания заказа  на электронную почту пользователей отправляется сообщение с информацией о заказе в асинхронном режиме через `Celery`;

## Установка
Эти инструкции помогут вам создать копию проекта и запустить ее на локальном компьютере для целей разработки и тестирования.

**Перед тем, как начать:**
Если вы не пользуетесь `Python 3`, вам нужно будет установить инструмент `virtualenv` при помощи `pip install virtualenv`. 
Если вы используете `Python 3`, у вас уже должен быть модуль [venv](https://docs.python.org/3/library/venv.html), установленный в стандартной библиотеке.

Для работы c `Celery` необходим посредник (брокер). 
Устнаовите `RabbitMQ` - он является рекомендуемым брокером для `Celery`
```
echo 'deb http://www.rabbitmq.com/debian/ testing main' | sudo tee /etc/apt/sources.list.d/rabbitmq.list
wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get install rabbitmq-server
```
Запустите сервер `RabbitMQ`
```
sudo systemctl enable rabbitmq-server
sudo systemctl start rabbitmq-server
```
[Подробнее об уствновке](https://www.rabbitmq.com/download.html) на официальном сайте `RabbitMQ`

### Запуск проекта (на примере Linux)
- Создайте на своем компютере папку проекта `mkdir ...` и перейдите в нее `cd ...`
- Склонируйте этот репозиторий в текущую папку
- Создайте виртуальное окружение `python3 -m venv venv`
- Активируйте виртуальное окружение `source venv/bin/activate`
- Установите зависимости `pip install -r requirements.txt`
- Накатите миграции `python manage.py migrate`
- Создайте суперпользователя Django `python manage.py createsuperuser --username admin --email 'admin@example.com'`
- Запустите сервер разработки Django `python manage.py runserver`
- Откройте другую консоль и запустите процесс `Celery` из папки проекта с помощью команды `celery -A  tkanioptom worker -l info`
