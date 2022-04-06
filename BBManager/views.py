from django.shortcuts import render
from django.contrib import  messages
from django.shortcuts import redirect, render
from Blood.models import Blood
from Donor.models import Donor 
from UserAccount.models import UserRegistration
from Hospital.models import Hospital , BloodRequest

def Userstate(request):  # for getting the state of the user 
    state = request.user
    account = UserRegistration.objects.get(Account_id=state.id) 
    context={'account':account}
    return context
def BBmanager(request):
    context=Userstate(request)
    return render(request ,  'bbmanager/bbmanager.html' , context) # sending the state of the user for the page rendered
def BBDashbord(request , type):
    bloodcount=0  # total blood count
    latest_blood=None   # latest added blood 
    bloodrequest=None # for holding blood request object
    try:
        latest_blood = Blood.objects.last # finding the last addeed blood form blood table
        bloodcount=len(Blood.objects.get(BloodGroup=latest_blood))
    except Blood.DoesNotExist:
        latest_blood = None
    try:
        if(type=='all'):
            bloodrequest = BloodRequest.objects.all()  
        else:
            bloodrequest = BloodRequest.objects.all()[0:5]
    except:
        bloodrequest= None
    context={'donors_count': Donor.objects.count() ,
                   'hospitals_count': Hospital.objects.count(),
                   'recent_blood_count':bloodcount,
                   'recent_blood':latest_blood ,
                   'bloodrequest':bloodrequest,
                   'hopsitals':Hospital.objects.all(),
                   'account':Userstate(request)['account']
    }
    return render(request, 'bbmanager/dashbord.html' ,context)