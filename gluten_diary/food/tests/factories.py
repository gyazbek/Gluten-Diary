import factory
from gluten_diary.users.tests.factories import UserFactory

class TypesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "food.Type"
    name = 'Test Food Type'

class BrandsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "food.Brand"
    name = 'Test Brand Type'


class FoodFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = "food.Food"
    title = 'Test title'
    notes = 'Test Notes'
    author = factory.SubFactory(UserFactory)
    types = factory.SubFactory(TypesFactory)
    brands = factory.SubFactory(BrandsFactory)
    reaction_scale = 5
    votes = 0