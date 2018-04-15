from django.urls import path

from . import views

app_name = 'food'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:food_id>/vote/', views.vote, name='vote'),
    path('create/', views.FoodCreate.as_view(), name="create"),
    path('update/<int:pk>/', views.FoodUpdate.as_view(), name="update"),

    path('brand-autocomplete/', views.BrandAutocomplete.as_view(), name="brand-autocomplete"),
    path('type-autocomplete/', views.TypeAutocomplete.as_view(), name="type-autocomplete"),


]