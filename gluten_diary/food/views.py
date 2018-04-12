from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone
from food.models import Type, Brand, Food



class IndexView(generic.ListView):
    template_name = 'food/index.html'
    context_object_name = 'food_list'
    paginate_by = 5  

    def get_queryset(self):
        """Return the last five published food items."""
        return Food.objects.filter(created_on__lte=timezone.now()).order_by('-created_on')

class DetailView(generic.DetailView):
    model = Food
    template_name = 'food/detail.html'


class ResultsView(generic.DetailView):
    model = Food
    template_name = 'food/results.html'

def vote(request, question_id):
    food = get_object_or_404(Food, pk=food_id)
    selected_choice.votes =  F('votes') + 1
    selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('food:results', args=(food.id,)))