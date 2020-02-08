from datetime import datetime

from django.forms import MultiValueField
from django.utils import timezone
from django.db import models


class Printer(models.Model):
    name = models.CharField("название", max_length=200)
    api_key = models.CharField("ключ доступа", max_length=40)
    check_type = models.CharField("тип чека", max_length=15)

    def __repr__(self):
        return self.name[:50]


class Order(models.Model):
    phone = models.CharField("Номер клиента", max_length=13)
    addres = models.CharField("адрес доставки", max_length=255)
    order_list = models.ManyToManyField(to='Dish')
    status_kitchen = models.CharField(max_length=15, default='new')
    status_receipt = models.CharField(max_length=15, default='new')
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Order number {self.id}'

class Dish(models.Model):
    name = models.CharField('Название', max_length=200)
    image = models.CharField(max_length=255, default='')
    price = models.DecimalField("Цена", max_digits=5, decimal_places=2)
    descriptions = models.TextField()

    def __str__(self):
        return self.name[:50]
