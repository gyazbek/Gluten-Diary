from django.db import models



class FoodDiary(models.Model):
    title = models.CharField(max_length=250)
    notes = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')

class Food(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')

class FoodType(models.Model):
    name = models.CharField(max_length=250)

class FoodBrand(models.Model):
    name = models.CharField(max_length=250)
