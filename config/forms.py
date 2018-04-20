from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.mail import send_mail

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    
    def send_email(self):
        return send_mail('New Contact Message', self.cleaned_data['content'], self.cleaned_data['email'], ['admin@glutendiary.com',])


    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-contact-form'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))