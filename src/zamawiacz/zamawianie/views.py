# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from langacore.kit.django.helpers import render

from zamawiacz.zamawianie.models import Unit, Multiplier, Customer, Order, Product, Entry

HEADER_HEIGHT = 2
PAGE_HEIGHT = 30

def _paginate(orders):
    order_length = len(orders)
    pages = []
    page = {'orders': [], 'height': 0, 'num': 1}
    for i in xrange(0, order_length, 2):
        height = HEADER_HEIGHT + orders[i].entries_count()
        if order_length > i+1:
            height = max(height, HEADER_HEIGHT + orders[i+1].entries_count())
        if page['height'] + height > PAGE_HEIGHT:
            pages.append(page)
            page = {'orders': [], 'height': 0, 'num': page['num'] + 1}
        page['height'] += height
        page['orders'].append(orders[i])
        if order_length > i+1:
            page['orders'].append(orders[i+1])
    pages.append(page)
    return pages

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
        # Switch to a simple entry count
        #return x.entries_summary_count() - y.entries_summary_count()
        return x.entries_count() - y.entries_count()

    orders.sort(order_compare)
    pages = _paginate(orders)

    return render(request, 'zamawianie/print.html', locals())
