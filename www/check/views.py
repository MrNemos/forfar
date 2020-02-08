from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.views.generic import View
import json
from .models import *

class Receipt_render_View(TemplateView):
    template_name = "client.html"

    def get(self, request, *args, **kwargs):
        order = get_object_or_404(Order, id=kwargs["id"])
        receipt = order.order_list.load()
        return render(request, self.template_name, {'order': order, 'order_list': receipt})

class ReceiptView(View):
    def post(self, request, *args, **kwargs):
        if request.metod == 'POST':
            print(request.action)
            if request.action == 'create order':
                request.content
        return HttpResponse(status=404)

def get(request):
    if Printer.objects.filter(api_key=request.header['key_pass']).exists():
        if request.header['type_printer'] == 'kitchen':
            queue = Order.objects.filter(status_kitchen='render')
            queue.status_kitchen = 'printed'
        else:
            queue = Order.objects.filter(status_client='render')
            queue.status_client = 'printed'
        return
    return Http404

