from django.urls import reverse
from django.utils.translation import ugettext as _

from allauth.account.forms import LoginForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        for field_name in self.fields:
            field = self.fields.get(field_name)

            loginField = self.fields.get("login")
            passwordField = self.fields.get("password")
            loginField.widget.attrs['placeholder'] = loginField.label
            loginField.label = ''
            passwordField.widget.attrs['placeholder'] = passwordField.label
            passwordField.label = ''
            
        # self.helper.form_show_labels = False
        # self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-xs-8'