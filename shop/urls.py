from django.conf.urls.static import static
from django.urls import path, re_path

from tkanioptom import settings
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('info/', how_to_buy, name='info'),
    path('contacts/', contacts, name='contacts'),
    path('basket_empty/', basket_empty, name='basket_empty'),
    path('warehouse/', warehouse, name='warehouse'),
    path('road/', road, name='road'),
    path('gabardin/<slug:g_slug>/', gabardin_detail, name='gabardin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
