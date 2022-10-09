from django.urls import path
from .views import *
from .forms import *


urlpatterns = [
    path('', basket_detail, name='basket_detail'),
    path('add/<int:gabardin_id>/', basket_add, name='basket_add'),
    path('remove/<int:gabardin_id>/', basket_remove, name='basket_remove'),
]