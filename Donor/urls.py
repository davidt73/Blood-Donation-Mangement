from . import views
from django.urls import path
urlpatterns = [
path('donor/', views.Donors, name='donor'),
path('register',views.Register , name='register'),
path('donordashbord/<type>' , views.DonorDashbord , name='donordashbord'),
path('donationrequest/<type>' , views.DonationRequest , name='donationrequest'),
path('makerequest', views.MakeDonationRequest , name='makerequest'),
path('getevent/<type>' , views.GetEvent , name='getevent'),
path('camps/<type>'  , views.GetCamp , name='getcamp' ),
path('donoreditaccount/' , views.EditAccount , name='donoreditaccount'),
]