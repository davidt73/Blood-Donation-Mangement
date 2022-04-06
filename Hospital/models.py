from django.db import models
import uuid
from Blood.models import Blood
# Create your models here.
class Hospital(models.Model):
    Hospital_id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    HospitalName = models.CharField(max_length=20, null=True , blank=True)
    Woreda = models.IntegerField(null=True , blank=True)
    Kebele = models.IntegerField(null=True , blank=True)
    HospitalRepresentative = models.CharField(max_length=10)
    PhoneNo= models.IntegerField(null=True , blank=True)
    BranchNo= models.CharField(max_length=10)
    City = models.CharField(max_length=30)

class BloodRequest(models.Model):
    Blood_Req_Id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    Hospital_id = models.OneToOneField(Hospital, on_delete=models.DO_NOTHING)
    Blood_id =  models.OneToOneField(Blood , on_delete=models.DO_NOTHING)
    Conatact_NO = models.IntegerField(null=True , blank=True)
    Blood_Group = models.CharField(max_length=10 , null=True , blank=True)
    Quantity = models.CharField(max_length=10 , null=True , blank=True)
    Request_Date = models.DateField()
    Status = models.CharField(max_length=10 , null=True , blank= True)

 