from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('basket/', include('basket.urls')),
    path('orders/', include('orders.urls')),
    path('', include('shop.urls'))
]
