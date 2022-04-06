from django.forms import ModelForm
from .models import Hospital
class HospitalCreationForm(ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'