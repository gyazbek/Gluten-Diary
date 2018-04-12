from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone
from food.models import Type, Brand, Food



class IndexView(generic.ListView):
    template_name = 'pages/home.html'
    context_object_name = 'latest_food_list'

    def get_queryset(self):
        """Return the last five published food items."""
        return Food.objects.filter(created_on__lte=timezone.now()).order_by('-created_on')[:5]