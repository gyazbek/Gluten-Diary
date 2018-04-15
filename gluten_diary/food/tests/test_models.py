from test_plus.test import TestCase
from .factories import TypesFactory, BrandsFactory, FoodFactory
import datetime
from django.utils import timezone

class TestTypes(TestCase):
    def setUp(self):
        self.type = TypesFactory(name='Test Type')
    def test__str__(self):
        self.assertEqual(
            self.type.__str__(),
            "Test Type",
        )

class TestBrands(TestCase):
    def setUp(self):
        self.type = BrandsFactory(name='Test Brand')
    def test__str__(self):
        self.assertEqual(
            self.type.__str__(),
            "Test Brand",
        )

class TestFood(TestCase):
    def setUp(self):
        self.food = FoodFactory(title='Test Food')
    def test__str__(self):
        self.assertEqual(
            self.food.__str__(),
            "Test Food",
        )
    def test_get_absolute_url(self):
        self.assertEqual(self.food.get_absolute_url(), "/food/{0}/".format(self.food.pk))

    def test_was_created_recently_with_future(self):
        """
        was_created_recently() returns False for Foods whose created_on
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_food = FoodFactory(created_on=time)
        print(future_food.created_on)
        self.assertIs(future_food.was_created_recently(), False)


# class TestUser(TestCase):

#     def setUp(self):
#         self.user = self.make_user()

#     def test__str__(self):
#         self.assertEqual(
#             self.user.__str__(),
#             "testuser",  # This is the default username for self.make_user()
#         )

#     def test_get_absolute_url(self):
#         self.assertEqual(self.user.get_absolute_url(), "/users/testuser/")
