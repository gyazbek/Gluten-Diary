from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone
from django.views.generic.edit import FormView
from django.contrib import messages
from django.urls import reverse_lazy

from food.models import Type, Brand, Food
from .forms import ContactForm


class IndexView(generic.ListView):
    template_name = 'pages/home.html'
    context_object_name = 'latest_food_list'

    def get_queryset(self):
        """Return the last five published food items."""
        return Food.objects.filter(published=True,created_on__lte=timezone.now()).order_by('-created_on')[:5]


class ContactView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        if form.send_email() > 0:
            messages.add_message(self.request, messages.SUCCESS, 'Thank you for contacting us, if required we will get back to you shortly.')
        else:
            messages.add_message(self.request, messages.WARNING, 'Unable to send message, please try again later.')
        return super().form_valid(form)