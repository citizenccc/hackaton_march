from django.contrib import admin

from applications.order.models import OrderProduct, Order


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1
    fields = ('product', 'quantity', 'total_cost')


class OrderAdminDisplay(admin.ModelAdmin):
    inlines = [OrderProductInline, ]
    list_display = ('user', 'status')
    list_editable = ('status', )

admin.site.register(Order, OrderAdminDisplay)
