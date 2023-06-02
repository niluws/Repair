from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    active_code = models.CharField(max_length=100)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر')
    post_code = models.CharField(max_length=256, verbose_name='کد پستی')
    address = models.CharField(max_length=256, verbose_name='ادرس')
    phone = models.CharField(max_length=256, unique=True, verbose_name='شماره تلفن')

    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل ها'

    def __str__(self):
        return str(self.user.first_name + self.user.last_name)


