from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
import datetime
from django.utils import timezone

class Type(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

class Food(models.Model):
    title = models.CharField(max_length=250)
    notes = models.CharField(max_length=2500)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    food_types = models.ManyToManyField(Type)
    food_brands = models.ManyToManyField(Brand)
    reaction_scale = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(10), MinValueValidator(0)]
     )
    votes = models.IntegerField(default=0)


    def was_created_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_on <= now

    # Admin interface configuration
    was_created_recently.admin_order_field = 'created_on'
    was_created_recently.boolean = True
    was_created_recently.short_description = 'Created recently?'

    def __str__(self):
        return self.title

