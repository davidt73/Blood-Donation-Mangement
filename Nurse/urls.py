from . import views
from django.urls import path
urlpatterns = [
path('nurse',views.Nurse, name='nurse'),
path('donorrequest/<type>', views.DonationRequest , name='donorrequest'),
path('checkrequest/<pk>' , views.CheckRequest , name='checkrequest'),
path('checkappointment/<type>', views.CheckAppointments , name='checkappointment'),
path('donorquestions/<type>', views.DonorQuestions , name='donorquestions'),
path('addquestions/<type>',views.AddQuestions , name='addquestions'),
path('updatequestion/<pk>' , views.UpdateQuestion , name='updatequestion'),
path('deletequestion/<pk>' , views.DeleteQuestion , name='deletequestion'),
path('confirmrequest/<pk>/<type>' , views.Confirmrequest , name='confirmrequest'),
]