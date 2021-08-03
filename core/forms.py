from django.forms import ModelForm

from .models import NewCustomer
from .models import *

class CustomerForm(ModelForm):
    class Meta:
        model = NewCustomer

        fields = '__all__'

    def clean(self):
        super(CustomerForm, self).clean()
         
        tc = self.cleaned_data.get('tc')
        telephone = self.cleaned_data.get('telephone')

        if len(str(tc)) != 11:
            self._errors['tc'] = self.error_class([
                'TC must contain of 11 characters.Please try again.'])
        
        if len(str(telephone)) != 11:
            self._errors['telephone'] = self.error_class([
                'Telephone must contain of 11 characters.Please add 0 per and try again.'])
        
        return self.cleaned_data