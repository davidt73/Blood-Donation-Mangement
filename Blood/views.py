from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Blood
from UserAccount.models import UserRegistration
# Create your views here.
def BloodStock(request):
    bbmanager = request.user
    account = UserRegistration.objects.get(Account_id=bbmanager.id)
    dic={'O+':0,'B+':0,'A+':0,'AB+':0,'O-':0,'B-':0,'A-':0,'AB-':0,}
    for i in Blood.objects.all():
        dic[i.BloodGroup]+=int(i.QuantityOfBlood[:-2])
    context = {
        'account':account,
        'Op':dic['O+'],'Ap':dic['A+'],'Bp':dic['B+'],'ABp':dic['AB+'],
        'Om':dic['O-'],'Am':dic['A-'],'Bm':dic['B-'],'ABm':dic['AB-'], 
    }
    return render(request ,'bbmanager/bloodstock.html' , context)