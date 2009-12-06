# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models as db

class Unit(db.Model):
    name = db.CharField(verbose_name=u'Nazwa', max_length=20, unique=True)
    shortform = db.CharField(verbose_name=u'Skrót', max_length=10, unique=True)

    class Meta:
        verbose_name = u'Jednostka'
        verbose_name_plural = u'Jednostki'
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class Multiplier(db.Model):
    value = db.FloatField(verbose_name=u"Wartość", unique=True)

    class Meta:
        verbose_name = u'Mnożnik'
        verbose_name_plural = u'Mnożniki'
        ordering = ('value',)

    def __unicode__(self):
        return u"%.2f" % self.value


class Customer(db.Model):
    name = db.CharField(verbose_name=u"Nazwa", max_length=50)
    locality = db.CharField(verbose_name=u"Miejscowość", max_length=50)

    class Meta:
        verbose_name = u'Klient'
        verbose_name_plural = u'Klienci'
        ordering = ('name', 'locality',)

    def __unicode__(self):
        return u"%s, %s" % (self.name, self.locality)


class Order(db.Model):
    created = db.DateTimeField(verbose_name=u"Data utworzenia", default=datetime.now)
    modified = db.DateTimeField(verbose_name=u"Data modyfikacji", default=datetime.now)
    customer = db.ForeignKey(Customer, verbose_name=u"Klient")
    due = db.DateTimeField(verbose_name=u"Na kiedy", default=datetime.now)

    def save(self):
        self.modified = datetime.now()
        super(Order, self).save()


    class Meta:
        verbose_name = u'Zamówienie'
        verbose_name_plural = u'Zamówienia'
        ordering = ('due', 'customer', 'created',)

    def __unicode__(self):
        return u"Zamówienie z dn. %s dla %s" % (self.created, self.customer)


class Product(db.Model):
    name = db.CharField(verbose_name=u"Nazwa", max_length=50)
    description = db.TextField(verbose_name=u"Opis", blank=True)
    unit = db.ForeignKey(Unit, verbose_name=u"Jednostka sprzedaży")


    class Meta:
        verbose_name = u'Produkt'
        verbose_name_plural = u'Produkty'
        ordering = ('name', 'unit',)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.unit)


class Entry(db.Model):
    order = db.ForeignKey(Order, verbose_name=u"Zamówienie")
    quantity = db.PositiveIntegerField(verbose_name=u"Ile")
    multiplier = db.ForeignKey(Multiplier, verbose_name=u"Mnożnik", blank=True, null=True)
    product = db.ForeignKey(Product, verbose_name=u"Produkt")
    remarks = db.CharField(verbose_name=u"Uwagi", max_length=100, blank=True)


    class Meta:
        verbose_name = u'Wpis'
        verbose_name_plural = u'Wpisy'
        ordering = ('order', 'product')

    def __unicode__(self):
        return u"%d x %s  %s" % (self.quantity, self.multiplier, self.product)

    def save(self):
        if self.multiplier is None:
            self.multiplier = Multiplier.objects.get(value=1)
        super(Entry, self).save()
