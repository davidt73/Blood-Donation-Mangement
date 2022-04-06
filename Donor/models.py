from cProfile import label
from multiprocessing.sharedctypes import Value
from django.db import models
from pyrsistent import field
from UserAccount.models import Account, Address
import uuid;
class Donor(models.Model):
    Donor_id =  models.OneToOneField(Account, on_delete=models.CASCADE)
    Donorname = models.CharField(max_length=20 , null=True , blank=True)
    DateOfBirth = models.DateTimeField(max_length=6, null=True , blank=True)
    Bloodgroup= models.CharField(max_length=10, null=True , blank=True)
    Address_id = models.OneToOneField(Address, on_delete=models.CASCADE , null=True , blank=True)
    Gender = models.CharField(max_length=10, null=True , blank=True)
    Age = models.IntegerField()
    Nationality = models.CharField(max_length=10, null=True , blank=True)
    Height = models.FloatField(max_length=10, null=True , blank=True)
    Weight = models.FloatField(max_length=10, null=True , blank=True)
    BMS = models.FloatField(max_length=10 , null=True , blank=True)
    BloodPressure = models.CharField(max_length=10 ,  null=True , blank=True)
    ProfilePic= models.FileField(null=True, blank=True, upload_to='profilepic/', default="profilepic/userdefault.png")



class Appointment(models.Model):
    App_id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    Donor_id = models.OneToOneField(Donor, on_delete=models.CASCADE)
    Date = models.DateField()
    Time = models.TimeField()
    status = models.CharField(null=True , max_length=10 , blank=True , default='in progress')



class DonationRequestFormQuesitons(models.Model):
   Question_id = models.UUIDField( default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
   HeartDisease = models.TextField (null=True , blank=True , )
   Kidney_Lung_Bloodpressure_Diabetes_Epilepsy = models.TextField( null=True , blank=True )
   Liverproblems = models.TextField(null=True , blank=True )
   STD = models.TextField(null=True , blank=True )
   Tattoo_Ear_skin_pierced_lastmonth= models.TextField( null=True , blank=True)
   Slpet_Unsafely_OtherThanPartner = models.TextField( null=True , blank=True )
   SeriousSkinRepair = models.TextField(null=True , blank=True )
   Preagnant = models.TextField(null=True , blank=True )
   Abortion = models.TextField( null=True , blank=True )
   BreastFeeding = models.TextField( null=True , blank=True  )
   BloodHealthfulnessInfo = models.TextField( null=True , blank=True)
   Type = models.CharField(max_length=10 , null=True , blank=True)




Answer_choices = [
    ( None, 'Answer'),
    ('yes', 'yes'),
    ('no', 'no'),
    ]
class DonationRequestFormResult(models.Model):
    Result_id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    Donor_id = models.ManyToOneRel( to= Donor, field_name='Donor_id' , field='Donor_id' ,on_delete=models.CASCADE)
    HeartDisease = models.CharField(max_length=3, null=True , blank=True ,choices=Answer_choices)
    Kidney_Lung_Bloodpressure_Diabetes_Epilepsy = models.CharField(max_length=3, null=True , blank=True ,  choices=Answer_choices)
    Liverproblems = models.CharField(max_length=3, null=True , blank=True ,choices=Answer_choices)
    STD = models.CharField(max_length=3, null=True , blank=True ,choices=Answer_choices)
    Tattoo_Ear_skin_pierced_lastmonth= models.CharField(max_length=3, null=True , blank=True ,choices=Answer_choices)
    Slpet_Unsafely_OtherThanPartner = models.CharField(max_length=3, null=True , blank=True ,choices=Answer_choices)
    SeriousSkinRepair = models.CharField(max_length=3, null=True , blank=True ,choices=Answer_choices)
    Preagnant = models.CharField(max_length=3, null=True , blank=True,choices=Answer_choices)
    Abortion = models.CharField(max_length=3, null=True , blank=True,choices=Answer_choices)
    BreastFeeding = models.CharField(max_length=3, null=True , blank=True,choices=Answer_choices)
    BloodHealthfulnessInfo = models.CharField(max_length=10, null=True , blank=True,choices=Answer_choices)
    status = models.CharField(null=True , max_length=10 , blank=True , default='in progress')

    





