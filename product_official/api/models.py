from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128)
    eng_name = models.CharField(max_length=128, blank=True)
    version = models.CharField(max_length=64)
    profile = models.TextField(blank=True)
    home_picture = models.FileField(upload_to='images/home_picture/%Y/%m/%d')
    QRcode = models.FileField(upload_to='images/QRcode/%Y/%m/%d')
    icon = models.FileField(upload_to='images/icon/%Y/%m/%d')

    def __str__(self):
        return self.name


class APP(Product):
    apk_file = models.FileField(upload_to='files/app/apk_file/%Y/%m/%d')
    apple_store_url = models.URLField(max_length=2000)
    android_store_url = models.URLField(max_length=2000)


class Game(Product):
    android_file = models.FileField(upload_to='files/game/android_file/%Y/%m/%d', blank=True)
    windows_file = models.FileField(upload_to='files/game/windows_file/%Y/%m/%d', blank=True)
    macOS_file = models.FileField(upload_to='files/game/macOS_file/%Y/%m/%d', blank=True)


class H5(Product):
    pass


class LittleProgram(Product):
    pass
