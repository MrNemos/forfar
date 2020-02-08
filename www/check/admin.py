from django.contrib import admin

from .models import Printer, Order, Dish

admin.site.register(Printer)
admin.site.register(Order)
admin.site.register(Dish)

