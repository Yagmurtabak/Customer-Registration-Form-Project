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

        if len(str(TC)) != 11:
            self._errors['TC'] = self.error_class([
                'TC Should Contain of 11 characters'])

        return self.cleaned_data