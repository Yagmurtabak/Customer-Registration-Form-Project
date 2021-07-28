from django.forms import ModelForm,fields
from django import forms
from .models import NewCustomer
from .models import *


class CustomerForm(ModelForm):
    class Meta:
        model = NewCustomer

        fields = '__all__'

    def clean(self):
        super(CustomerForm, self).clean()
         

        TC = self.cleaned_data.get('TC')
        Telephone = self.cleaned_data.get('Telephone')

        if len(str(TC)) != 11:
            self._errors['TC'] = self.error_class([
                'TC must contain of 11 characters.Please try again.'])
        
        if len(str(Telephone)) != 10:
            self._errors['Telephone'] = self.error_class([
                'TC must contain of 10 characters.Please try again.'])
        
        return self.cleaned_data