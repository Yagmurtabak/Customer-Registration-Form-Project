from django.forms import ModelForm, fields
from .models import yazı

class CreateForms(ModelForm):
    class Meta:
        model = yazı

        fields = '__all__'

