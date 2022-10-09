from django import forms
from shop.models import Gabardin
from .basket import Basket
from django.shortcuts import get_object_or_404, redirect
from .urls import *


class BasketAddGabardinForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='Введите количество')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
