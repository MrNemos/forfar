from django.db import models

class Printer:
    name = models.CharField("название", max_length=200)
    api_key = models.CharField("ключ доступа")
    check_type = models.CharField("тип чека")

class Order:
    phone = models.DecimalField("Номер клиента")
    addres = models.CharField("адрес доставки", max_length=255)
    order_list = models.ForeignKey("Dish", on_delete=models.CASCADE)
    total_price = models.DecimalField("Стоимостть", max_digits=5, decimal_places=2)
    status = models.CharField()

class Dish:
    name = models.CharField('Название', max_length=200)
    image = models.CharField(max_length=255)
    price = models.DecimalField("Цена", max_digits=5, decimal_places=2)
    descriptions = models.TextField()