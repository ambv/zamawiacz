from django.contrib import admin

from django_extensions.admin import ForeignKeyAutocompleteInlineMixin, ForeignKeyAutocompleteModelMixin

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


class EntryInline(ForeignKeyAutocompleteInlineMixin, admin.TabularInline):
    model = Entry
    related_search_fields = {'product': ('name',)}
    hide_id_textfields = ('product', )
    extra = 30


class OrderAdmin(ForeignKeyAutocompleteModelMixin, admin.ModelAdmin):
    def orders(self):
        result = {}
        for entry in self.entry_set.all():
            key = (entry.product, entry.multiplier, entry.unit) 
            if key not in result:
                result[key] = entry.quantity
            else:
                result[key] += entry.quantity
        return u', '.join((u"%d %s%s %s" % (v, (u"x %.2f " % k[1].value if k[1].value != 1 else u""), k[2] if k[2] is not None else u"", k[0]) for k, v in result.iteritems()))
    orders.short_description = u'Wpisy'
    
    inlines = (EntryInline,)
    list_display = ('due', 'customer', 'created', 'modified', orders)
    list_filter = ('due', 'customer', 'created', 'modified',)
    save_on_top = True

admin.site.register(Order, OrderAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', )
    list_filter = ('name',)
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)
