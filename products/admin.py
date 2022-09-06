from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . import models


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'country',
    )

    ordering = ('country',)

    search_fields = ('friendly_name',)


class TourAdmin(SummernoteModelAdmin):
    summernote_fields = (
        'description',
        'itinerary',
    )
    list_display = (
        'friendly_name',
        'price',
        'length_of_tour',
    )

    search_fields = ('friendly_name',)


admin.site.register(models.Location, LocationAdmin)
admin.site.register(models.Tour, TourAdmin)
admin.site.register(models.Date)
