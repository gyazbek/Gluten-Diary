from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.utils import timezone
from .models import User
from .forms import ProfileForm
from food.models import Type, Brand, Food
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"
    
    def get_context_data(self, **kwargs):
        """
        This has been overridden to add `car` to the templates context,
        so you can use {{ car }} etc. within the template
        """
        context = super(UserDetailView, self).get_context_data(**kwargs)
        food_list_obj = Food.objects.filter(author=self.get_object(), created_on__lte=timezone.now()).order_by('-created_on')
        paginator = Paginator(food_list_obj, 5)
        page = self.request.GET.get('page')
        try:
            food_list = paginator.page(page)
        except PageNotAnInteger:
            food_list = paginator.page(1)
        except EmptyPage:
            food_list = paginator.page(paginator.num_pages)
                
        context["food_list"] = food_list
        return context

class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    form_class = ProfileForm

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)
