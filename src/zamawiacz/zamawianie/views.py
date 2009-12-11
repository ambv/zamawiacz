# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from langacore.kit.django.helpers import render

from zamawiacz.zamawianie.models import Unit, Multiplier, Customer, Order, Product, Entry

def print_tomorrow(request):
    return print_for(request, timedelta(days=1), timedelta(days=2))

def print_today(request):
    return print_for(request, timedelta(days=0), timedelta(days=1))

def print_2days(request):
    return print_for(request, timedelta(days=1), timedelta(days=3))

def print_for(request, delta_start, delta_end):
    now = datetime.now()
    due = datetime(now.year, now.month, now.day, 0, 0, 0)
    orders = list(Order.objects.filter(due__gte=due+delta_start, due__lt=due+delta_end))
   
    def order_compare(x, y):
        return x.entries_summary_count() - y.entries_summary_count()

    orders.sort(order_compare)

    return render(request, 'zamawianie/print.html', locals())
