from django import forms
from django.urls import reverse
from django.utils.translation import ugettext as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML
from django_comments.forms import CommentForm


class CustomCommentForm(CommentForm):
    def __init__(self, target_object, data=None, initial=None, **kwargs):
        super(CustomCommentForm, self).__init__(target_object, data, initial, **kwargs)
        self.helper = FormHelper()
        # self.fields.pop('name')
        # self.fields.pop('email')
        # self.fields.pop('url')
        self.fields['honeypot'].widget = forms.HiddenInput()
        self.fields['comment'].widget.attrs['placeholder'] = 'Add a comment...'
        self.fields['comment'].label = '' 
        self.fields['comment'].widget.attrs['rows'] = 3
        
        # nameField = self.fields.get("name")
        # nameField.widget.attrs['placeholder'] = nameField.label
        # nameField.label = ''   
        # # self.helper.form_show_labels = False
        # # self.helper.form_class = 'form-horizontal'
        # self.helper.field_class = 'col-xs-8'

