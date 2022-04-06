from Hospital.models import Hospital
from . import views
from django.urls import path
from .views import HospitalRequest  ,Hospitals
urlpatterns = [
path('hospitalrequest/<type>', views.HospitalRequest, name='hospitalrequest'), 
path('hospitals/<type>' , views.Hospitals , name='hospitals'),
path('addhospital' , views.AddHospital , name='addhospital'),
path('updatehospital/<pk>' , views.UpdateHospital , name='updatehospital'),
path('deletehospital/<pk>' , views.DeleteHospital , name='deletehospital'),
]