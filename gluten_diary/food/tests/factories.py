import factory
import datetime

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
    title = 'Test Food'
    notes = 'Test Notes'
    author = factory.SubFactory(UserFactory)
    reaction_scale = 5
    votes = 0

    
    @factory.post_generation
    def types(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            # A list of groups were passed in, use them
            for type in extracted:
                self.types.add(type)

    @factory.post_generation
    def brands(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            # A list of brands were passed in, use them
            for brand in brands:
                self.brands.add(brand)