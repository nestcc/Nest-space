from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class NepUser(AbstractUser):
    nick_name = models.CharField(max_length=20, default='None')
    mobile = models.CharField(max_length=20, null=True, blank=True)
    icon = models.ImageField(null=True, upload_to='user_icon/', default='user_icon/default-icon.jpg', blank=True)   # 头像
    discription = models.CharField(max_length=255, null=True, blank=True)
    score = models.IntegerField(default=0)                          # 积分
    qq_num = models.CharField(max_length=12, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'nep_user'

