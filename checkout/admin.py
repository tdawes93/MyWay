from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = (
        'tour_total',
        'tour_discount',
    )


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)
    readonly_fields = (
        'order_number',
        'date',
        'product_total',
        'total_discount',
        'grand_total',
    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
