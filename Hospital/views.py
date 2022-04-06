from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import  messages
from Hospital.forms import HospitalCreationForm
from .models import BloodRequest , Hospital
from UserAccount.models import UserRegistration
def bbmanagerstate(request):
    bbmanager = request.user
    account = UserRegistration.objects.get(Account_id=bbmanager.id)
    context={'account':account}
    return context
def HospitalRequest(request, type):
    bloodrequest =None
    try:
        if(type=='all'):
            bloodrequest = BloodRequest.objects.all()
        else:
            bloodrequest = BloodRequest.objects.all()[0:5]

    except:
        bloodrequest= None
    context={
                   'bloodrequest':bloodrequest,
                   'hopsitals':Hospital.objects.all(),
                   'account':bbmanagerstate(request)['account']
    }
    return render (request , 'bbmanager/hospitalrequest.html' , context)

def Hospitals(request , type):
    hopitals = None
    try:
        if(type=='all'):
            hospitals = Hospital.objects.all()
        else:
            hospitals = Hospital.objects.all()[0:5]
    except:
        hospitals= None
    context={'hospitals' : hospitals , 'account':bbmanagerstate(request)['account']}
    return render(request ,  'bbmanager/hospitals.html' , context)
def AddHospital(request):
    form = HospitalCreationForm
    if request.method == 'POST':
        form= HospitalCreationForm(request.POST)
        if (form.is_valid()):
            try:
                events = form.save(commit=False)
                events.save()
                messages.success(request, 'Successfully Added Hospital')
                return redirect('/hospitals/notall')
            except:   
                messages.error(request, 'An error has occurred during adding hospital')
        else:
            messages.error(
                request, 'An error has occurred during adding hospital')
    context = {'form': form , 'type':'add' , 'account':bbmanagerstate(request)['account']}
    return render(request, 'bbmanager/addhospital.html',context)
def UpdateHospital(request , pk ):
    hospital = Hospital.objects.get(Hospital_id=pk)
    form = HospitalCreationForm(instance=hospital)
    if request.method == 'POST':
        form = HospitalCreationForm(request.POST, instance=hospital)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hospital was updated successfully!')
            return redirect('/hospitals/notall')
        else:
            messages.success(request, 'Hospital was not updated successfully!')

    context = {'form': form , 'type':'update' , 'account':bbmanagerstate(request)['account']}
    return render(request, 'bbmanager/addhospital.html', context)
def DeleteHospital(request , pk):
    hospital = Hospital.objects.get(Hospital_id=pk)
    try:
        hospital.delete()
        messages.success(request, 'Hospital was deleted successfully!')
        return redirect('/hospitals/notall')
    except:
        messages.success(request, 'Hospital was not deleted successfully!')
    return render(request, 'bbmanager/addhospital.html')