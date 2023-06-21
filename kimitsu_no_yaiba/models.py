from django.db import models
from accounts.models import CustomUser
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class kimitsu(models.Model):
    char_name = models.CharField(max_length=20 , null = False, blank = True)
    otaku_name = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    char_discription = models.TextField(null=False , blank=True)

    def __str__(self):
        return self.char_name
    def get_absolute_url(self):
        return reverse('kimitsu_list')
    