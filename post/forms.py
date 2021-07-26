from django import forms
from django.forms import ModelForm, fields
from .models import NewCustomer


class CustomerForm(ModelForm):
    class Meta:
        model = NewCustomer
        
        fields = '__all__'

