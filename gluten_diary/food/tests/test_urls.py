from django.urls import reverse, resolve

from test_plus.test import TestCase

    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:food_id>/vote/', views.vote, name='vote'),
    # path('create/', views.FoodCreate.as_view(), name="create"),
    # path('update/<int:pk>/', views.FoodUpdate.as_view(), name="update"),
    # path('brand-autocomplete/', views.BrandAutocomplete.as_view(), name="brand-autocomplete"),
    # path('type-autocomplete/', views.TypeAutocomplete.as_view(), name="type-autocomplete"),

class TestUserURLs(TestCase):
    """Test URL patterns for users app."""

    def setUp(self):
        pass

    def test_detail_reverse(self):
        """food:detail should reverse to /food/1/."""
        self.assertEqual(
            reverse("food:detail", kwargs={"pk": "1"}), "/food/1/"
        )

    def test_detail_resolve(self):
        """/food/1/ should resolve to food:detail."""
        self.assertEqual(resolve("/food/1/").view_name, "food:detail")

    def test_update_reverse(self):
        """food:update should reverse to /food/update/1/."""
        reverse("food:update", kwargs={"pk": "1"}), "/food/update/1/"

    def test_update_resolve(self):
        """/food/update/1/ should resolve to food:update."""
        self.assertEqual(resolve("/food/update/1/").view_name, "food:update")
