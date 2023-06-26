from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Users(AbstractUser):
    id = models.CharField(max_length=30,verbose_name='openid', primary_key=True)
    avatar_url = models.CharField(max_length=50, verbose_name='头像', blank=True, null=True)
    nick_name = models.CharField(max_length=10, verbose_name='昵称', blank=True, null=True)
    tenat_id = models.IntegerField(blank=True, null=True)