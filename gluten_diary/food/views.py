from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView,UpdateView
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone
from django.http import Http404
from dal import autocomplete
from .models import Type, Brand, Food
from .forms import FoodSearchForm,FoodCreateForm,FoodUpdateForm


class BrandAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Brand.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs

class TypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Type.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs



class FoodUpdate(LoginRequiredMixin,UpdateView):
    model = Food
    form_class = FoodUpdateForm
    template_name = "food/update.html"


class FoodCreate(LoginRequiredMixin,CreateView):
    model = Food
    form_class = FoodCreateForm
    template_name = "food/create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

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
            q = form.cleaned_data['q']
            order = form.cleaned_data['order']
            brand = form.cleaned_data['brand']
            type = form.cleaned_data['type']

        qs = Food.objects.all().filter(published=True)

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
    def get_object(self, queryset=None):
        obj = super(DetailView, self).get_object(queryset=queryset)
        if obj.published or self.request.user.is_authenticated and obj.author == self.request.user:
            return obj
        else:
            raise Http404()
        


def vote(request, question_id):
    food = get_object_or_404(Food, pk=food_id)
    selected_choice.votes =  F('votes') + 1
    selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('food:results', args=(food.id,)))