from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'father_name', 'number_phone', 'email', 'company', 'city', 'content']
