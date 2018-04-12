from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone
from .models import Type, Brand, Food
from .forms import FoodSearchForm


class IndexView(generic.ListView):
    template_name = 'food/index.html'
    context_object_name = 'food_list'
    paginate_by = 5  
    form_class = FoodSearchForm

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['form'] = self.form_class(self.request.GET)
        return context


    """Return the last five published food items."""
    def get_queryset(self):

        order = '-created_on'
        q = None
        form = self.form_class(self.request.GET)
        
        if form.is_valid():
            print(form.cleaned_data)
            q = form.cleaned_data['q']
            order = form.cleaned_data['order']
            brand = form.cleaned_data['brand']
            type = form.cleaned_data['type']

        qs = Food.objects.all()

        if not order:
            order = '-created_on'
            
        if brand:
            qs = qs.filter(food_brands__in=[brand.pk])

        if type:
            qs = qs.filter(food_types__in=[type.pk])

        if q and q != '':
            qs = qs.filter(title__icontains = q)
            
        return qs.order_by(order)

         

class DetailView(generic.DetailView):
    model = Food
    template_name = 'food/detail.html'




def vote(request, question_id):
    food = get_object_or_404(Food, pk=food_id)
    selected_choice.votes =  F('votes') + 1
    selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('food:results', args=(food.id,)))