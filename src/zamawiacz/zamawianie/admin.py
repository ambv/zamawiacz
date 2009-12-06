from django.contrib import admin

from zamawiacz.zamawianie.models import Unit, Multiplier, Customer, Order, Product, Entry


class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'shortform',)
    search_fields = ('name',)

admin.site.register(Unit, UnitAdmin)


class MultiplierAdmin(admin.ModelAdmin):
    pass

admin.site.register(Multiplier, MultiplierAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'locality',)
    search_fields = ('name', 'locality',)

admin.site.register(Customer, CustomerAdmin)


class EntryInline(admin.TabularInline):
    model = Entry
    extra = 30


class OrderAdmin(admin.ModelAdmin):
    def orders(self):
        result = []
        for entry in self.entry_set.all():
            result.append(u"%d %s %s" % (entry.quantity, (u"x %.2f" % entry.multiplier.value if entry.multiplier.value != 1 else u""), entry.product))
        return u', '.join(result)
    orders.short_description = u'Wpisy'
    
    inlines = (EntryInline,)
    list_display = ('due', 'customer', 'created', 'modified', orders)
    list_filter = ('due', 'customer', 'created', 'modified',)
    save_on_top = True

admin.site.register(Order, OrderAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'unit')
    list_filter = ('unit',)
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)
