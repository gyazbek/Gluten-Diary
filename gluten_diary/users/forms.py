import sys
from django.urls import reverse
from django.utils.translation import ugettext as _
from django import forms
from django.conf import settings
from allauth.account.forms import LoginForm,SignupForm
from allauth.account import app_settings
from .models import User
from django.core.files.images import get_image_dimensions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML
from crispy_forms.layout import Submit


class ProfileForm(forms.ModelForm):
    def clean_avatar(self):
        image = self.cleaned_data['avatar']
        if image:
            w, h = get_image_dimensions(image)
            if w < settings.MIN_AVATAR_IMAGE_WIDTH or h < settings.MIN_AVATAR_IMAGE_HEIGHT:
                raise forms.ValidationError(u' The image needs to be at least ' +     str(settings.MIN_AVATAR_IMAGE_WIDTH) + 'px * ' + str(settings.MIN_AVATAR_IMAGE_HEIGHT) + 'px (or less).')
        return image

    class Meta:
        model = User
        fields = ['name', 'username', 'email','avatar']
        labels = {
            'name': _('Name (If filled in, used publicly instead of username)'),
        }
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        super(ProfileForm, self).__init__(*args, **kwargs)

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 
        self.fields.get("username").label = ''
        self.fields.get("email").label = ''
        self.fields.get("password1").label = ''
        if app_settings.SIGNUP_PASSWORD_ENTER_TWICE:
            self.fields.get("password2").label = ''

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
       
        loginField = self.fields.get("login")
        passwordField = self.fields.get("password")
        loginField.widget.attrs['placeholder'] = loginField.label
        loginField.label = ''
        passwordField.widget.attrs['placeholder'] = passwordField.label
        passwordField.label = ''
        # self.helper.form_show_labels = False
        # self.helper.form_class = 'form-horizontal'
