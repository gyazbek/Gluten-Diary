from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone
from django.views.generic.edit import FormView
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
    # success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)