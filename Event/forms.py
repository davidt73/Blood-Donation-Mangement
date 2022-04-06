from django.forms import ModelForm
from .models import Event , Camp
class EventCreationForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class CampCreationForm(ModelForm):
    class Meta:
        model = Camp
        fields = '__all__'