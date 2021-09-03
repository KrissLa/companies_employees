""" Дополнительные формы """

from django.forms import ModelForm
from django_countries.widgets import CountrySelectWidget
from .models import Office


class OfficeForm(ModelForm):
    """
    Определение формы для класса модели Office
    """
    class Meta:
        """
        Определение полей в форме и замена виджета для поля country
        """
        model = Office
        fields = ('company', 'name', 'address', 'country', 'is_active')
        widgets = {'country': CountrySelectWidget()}
