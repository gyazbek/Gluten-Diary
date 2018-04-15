from django.urls import reverse
from django.utils.translation import ugettext as _
from django import forms
from django.conf import settings
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from dal import autocomplete


from .models import Food, Type, Brand

REACTION_CHOICES=[('0','No reaction'),
                ('2','Somewhat reacted'),
            ('5','Medium reaction'),
             ('7','Reacted'),
         ('10','Reacted strongly')]


class FoodUpdateForm(forms.ModelForm):
    reaction_scale = forms.ChoiceField(label="How strongly did you react?", choices=REACTION_CHOICES, widget=forms.RadioSelect())
    class Meta:
        model = Food
        exclude = ['author','votes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 5}),
            'brands': autocomplete.ModelSelect2Multiple(url='food:brand-autocomplete'),
            'types': autocomplete.ModelSelect2Multiple(url='food:type-autocomplete')
        }
    def __init__(self, *args, **kwargs):
        super(FoodUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.include_media = False

class FoodCreateForm(forms.ModelForm):
    reaction_scale = forms.ChoiceField(label="How strongly did you react?", choices=REACTION_CHOICES, widget=forms.RadioSelect())
    class Meta:
        model = Food
        exclude = ['author','votes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 5}),
            'brands': autocomplete.ModelSelect2Multiple(url='food:brand-autocomplete'),
            'types': autocomplete.ModelSelect2Multiple(url='food:type-autocomplete')

        }

    def __init__(self, *args, **kwargs):
        super(FoodCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.include_media = False




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

                