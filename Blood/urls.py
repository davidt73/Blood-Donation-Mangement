from Blood.models import Blood
from . import views
from django.urls import path
urlpatterns = [
path('bloodstock/',  views.BloodStock, name='bloodstock'), 
]