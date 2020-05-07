from django.contrib import admin
from .models import *


def change_status_o(modeladmin, request, queryset):
    queryset.update(status='o')
change_status_o.short_description = "Изменить статус на отказано"

def change_status_n(modeladmin, request, queryset):
    queryset.update(status='n')
change_status_n.short_description = "Изменить статус на новый"

def change_status_v(modeladmin, request, queryset):
    queryset.update(status='v')
change_status_v.short_description = "Изменить статус на выполняется"


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0

class OrderAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInOrderInline]
    actions = [change_status_n, change_status_o, change_status_v]

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)


class ProductInOrderAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]

    class Meta:
        model = ProductInOrder

admin.site.register(ProductInOrder, ProductInOrderAdmin)


class ProductInBasketAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductInBasket._meta.fields]

    class Meta:
        model = ProductInBasket

admin.site.register(ProductInBasket, ProductInBasketAdmin)
