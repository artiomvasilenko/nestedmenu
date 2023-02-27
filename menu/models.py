from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Название меню')

    def __str__(self):
        return self.title

class Item(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Название элемента')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title