from pyexpat import model
from attr import fields
from django.forms import ModelForm
from .models import DonationRequestFormQuesitons, Donor , Appointment , DonationRequestFormResult
class DonorCreationForm(ModelForm):
    class Meta:
        model = Donor
        fields = ['Donorname','DateOfBirth','Bloodgroup','Gender','Age','Nationality','Height','Weight','BMS','BloodPressure']

class DonorAccountEditForm(ModelForm):
    class Meta:
        model = Donor
        fields = ['ProfilePic']

class AppointmentCreationForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['Date','Time']

class RequestAnswerCreationForm(ModelForm):
        class Meta:
            model = DonationRequestFormResult
            fields = ['HeartDisease','Kidney_Lung_Bloodpressure_Diabetes_Epilepsy',
            'Liverproblems','STD','Tattoo_Ear_skin_pierced_lastmonth','Slpet_Unsafely_OtherThanPartner',
            'SeriousSkinRepair','Preagnant','Abortion','BreastFeeding','BloodHealthfulnessInfo']

class DonationRequestQuestionForm(ModelForm):
    class Meta:
        model = DonationRequestFormQuesitons
        fields = '__all__'