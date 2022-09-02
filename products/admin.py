from django.contrib import admin
from . import models


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'country',
    )

    ordering = ('country',)

    search_fields = ('friendly_name',)


class TourAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'price',
        'length_of_tour',
    )

    search_fields = ('friendly_name',)


admin.site.register(models.Location, LocationAdmin)
admin.site.register(models.Tour, TourAdmin)
admin.site.register(models.Date)
