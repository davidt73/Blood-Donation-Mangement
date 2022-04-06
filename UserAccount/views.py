from django.contrib import  messages
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.contrib.auth import login, authenticate, logout
from UserAccount.models import Account ,  UserRegistration
from UserAccount.forms import  CustomUserChangeForm, CustomUserCreationForm, CustomUserUpdate
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


class HomePage(ListView):   # class based view for just rendering the home page         
    model= Account           
    template_name = 'home.html' 
def Login(request , role):          # function based view for handling user login
    form = CustomUserCreationForm()
    if request.method == 'POST':
        username = request.POST['username'].lower()      # making sure the user name is in lowercase 
        password = request.POST['password1']
        try:
            user = Account.objects.get(username=username)   # Searching the user in Account table
        except:
            messages.error(request, 'Username does not exist')
        user = authenticate(request, username=username, password=password , Role=role)   # full user authenticaton including role
        if user is not None:
            login(request, user) 
            if(role.lower() =='bbmanager' ):    
                return redirect('/bbdashbord/all')  # redircting to other page after login
            elif(role.lower() =='donor'):
                return redirect('/donordashbord/all')
            elif(role.lower()=='nurse'):
                return redirect('/donorrequest/all')

        else:
            messages.error(request, 'Username OR password is incorrect')
    return render(request, 'login.html',{'Role':role,'form':form})  

def Logout(request):
    logred = '/login/' + request.user.Role  # getting the redirection path for every role
    logout(request)
    messages.info(request, 'Successfuly Logged out!')    
    return redirect(logred)

def ForgotPassword(request,role):  # not implemented 
    return render(request , 'forgot.html',{'Role':role})

def ResetPassword(request,role): # not implemtented
    return render(request,'reset.html',{'Role':role})


def Userstate(request):  # for getting the state of the user 
    state = request.user
    account = UserRegistration.objects.get(Account_id=state.id) 
    context={'account':account}
    return context


def EditAccount(request):
    state = request.user # hodling the state of the user
    useraccount = Account.objects.get(id=state.id)  # getting the user account from the state 
    account = Userstate(request)['account']
    form1= CustomUserChangeForm(instance=useraccount)  # using form created in forms.py
    form2=CustomUserUpdate (instance=account)
    form3 = PasswordChangeForm(request.user)

    if request.method == 'POST':
        form1 = CustomUserChangeForm(request.POST, instance=useraccount)
        form2 = CustomUserUpdate(request.POST, request.FILES, instance=account)  # recieving all files from the page including the new profile pic 
        form3 = PasswordChangeForm(request.user, request.POST)

        if (form1.is_valid() and form2.is_valid() and form3.is_valid()):
            try:
                user = form3.save()
                update_session_auth_hash(request, user)  # Important!
            except:
                messages.error(request,'Error occured during updating password')
            try:
                form1.save()
                messages.success(request,'Account updated successfuly')
            except:
                messages.error(request,'Error occured during updating account')
            try:
                form2.save()
                messages.success(request,'Profile updated successfuly')
            except:
                messages.error(request,'Error occured during updating profile pic')
        else:
                messages.error(request,'please input correct information')
        request.user.save() # saving the state of the user after it is updated 
    context = {'form1': form1 , 'form2':form2 ,'form3':form3 , 'account':account }
    if(request.user.Role.lower() == 'bbmanager'):
        return render(request, 'bbmanager/editaccount.html', context)
    elif(request.user.Role.lower() == 'nurse'):
        return render(request, 'nurse/editaccount.html', context)


    














































































