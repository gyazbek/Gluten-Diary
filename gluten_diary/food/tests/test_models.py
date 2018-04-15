from test_plus.test import TestCase
from .factories import TypesFactory, BrandsFactory, FoodFactory
class TestTypes(TestCase):

    def setUp(self):
        self.type = TypesFactory(name='Test Type')

    def test__str__(self):
        self.assertEqual(
            self.type.__str__(),
            "Test Type",  # This is the default name for self.make_user()
        )


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
