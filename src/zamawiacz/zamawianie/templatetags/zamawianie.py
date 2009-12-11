# -*- coding: utf-8 -*-                                                                                                                                                                                                                                                       

from django.template import Library

register = Library()

polish_weekdays = {0: u"poniedziałek",
    1: u"wtorek",
    2: u"środa",
    3: u"czwartek",
    4: u"piątek",
    5: u"sobota",
    6: u"niedziela"}

@register.filter
def polish_weekday(due_date):
    return polish_weekdays[due_date.weekday()]
