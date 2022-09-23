from django import forms
from .models import Tour, Date, Location
from .widgets import CustomClearableFileInput
from django_summernote.fields import SummernoteTextFormField

class TourForm(forms.ModelForm):

    class Meta:
        model = Tour
        fields = '__all__'

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        locations = Location.objects.all()
        location_friendly_names = [
            (l.id, l.get_friendly_name()) for l in locations
        ]

        self.fields['locations'].choices = location_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-border'
        self.fields['description'] = SummernoteTextFormField()
        self.fields['itinerary'] = SummernoteTextFormField()
