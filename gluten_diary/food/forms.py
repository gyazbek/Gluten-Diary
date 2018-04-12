from django.urls import reverse
from django.utils.translation import ugettext as _
from django import forms
from django.conf import settings
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML
from .models import Type, Brand

ORDER_CHOICES = (
    ('-created_on', _("Latest")),
    ('created_on', _("Oldest")),
)

class FoodSearchForm(forms.Form):
    q = forms.CharField(required=False)
    order = forms.ChoiceField(choices=ORDER_CHOICES, label="",widget=forms.Select(), required=False)
    brand = forms.ModelChoiceField(empty_label='All Brands',queryset=Brand.objects.all(), required=False)
    type = forms.ModelChoiceField(empty_label='All Types',queryset=Type.objects.all(), required=False)
    
    def __init__(self, *args, **kwargs):
            super(FoodSearchForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            qField = self.fields.get("q")
            qField.widget.attrs['placeholder'] = 'Search by name'
            qField.widget.attrs['class'] = 'form-control'

            orderField = self.fields.get("order")
            orderField.widget.attrs['placeholder'] = 'Latest'
            orderField.widget.attrs['class'] = 'custom-select filter-food'

            brandField = self.fields.get("brand")
            brandField.widget.attrs['class'] = 'custom-select filter-food'
          
            typeField = self.fields.get("type")
            typeField.widget.attrs['class'] = 'custom-select filter-food'

                