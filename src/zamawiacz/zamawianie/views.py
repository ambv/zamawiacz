# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from langacore.kit.django.helpers import render

from zamawiacz.zamawianie.models import Unit, Multiplier, Customer, Order, Product, Entry

polish_weekdays = {0: u"poniedziałek",
    1: u"wtorek",
    2: u"środa",
    3: u"czwartek",
    4: u"piątek",
    5: u"sobota",
    6: u"niedziela"}

def print_tomorrow(request):
    now = datetime.now()
    due = datetime(now.year, now.month, now.day, 0, 0, 0) + timedelta(days=1)
    orders = list(Order.objects.filter(due__gte=due, due__lt=due+timedelta(days=1)))
   
    due_day_of_week = polish_weekdays[due.weekday()] 

    def order_compare(x, y):
        return x.entries_summary_count() - y.entries_summary_count()

    orders.sort(order_compare)

    return render(request, 'zamawianie/print.html', locals())
