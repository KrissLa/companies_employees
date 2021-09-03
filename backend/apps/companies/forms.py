""" Дополнительные формы """

from django.forms import ModelForm
from django_countries.widgets import CountrySelectWidget
from .models import Office


class OfficeForm(ModelForm):
    class Meta:
        model = Office
        fields = ('company', 'name', 'address', 'country', 'is_active')
        widgets = {'country': CountrySelectWidget()}
