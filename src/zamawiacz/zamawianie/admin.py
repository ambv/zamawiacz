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
    extra = 10


class OrderAdmin(admin.ModelAdmin):
    inlines = (EntryInline,)
    list_display = ('due', 'customer', 'created', 'modified',)
    list_filter = ('due', 'customer', 'created', 'modified',)
    save_on_top = True

admin.site.register(Order, OrderAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'unit')
    list_filter = ('unit',)
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)
