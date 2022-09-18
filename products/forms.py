from django import forms
from .models import Tour, Date, Location


class TourForm(forms.ModelForm):

    class Meta:
        model = Tour
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        locations = Location.objects.all()
        location_friendly_names = [
            (l.id, l.get_friendly_name()) for l in locations
        ]
        dates = Date.objects.all()
        date_names = [(d.id, d.get_name()) for d in dates]

        self.fields['locations'].choices = location_friendly_names
        self.fields['dates'].choices = date_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-border'
