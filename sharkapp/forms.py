from django.forms import ModelForm
from .models import Sighting

class SightingForm(ModelForm):
  class Meta:
    model = Sighting
    fields = ['beach_name', 'city_state', 'country', 'comment']