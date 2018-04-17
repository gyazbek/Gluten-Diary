from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from sorl import thumbnail 


class User(AbstractUser):
    name = models.CharField(_("Name"), blank=True, max_length=255)
    avatar = thumbnail.ImageField(blank=True, null=True)

    def __str__(self):
        return self.username
    
    # returns name if set, or username if else
    def user_avail_name(self):
        if self.name:
            return self.name
        return self.username


    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
