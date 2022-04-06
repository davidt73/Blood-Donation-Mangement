from django.db import models
import uuid
from Donor.models import Donor
class Blood(models.Model):
    Blood_id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    Donor_id = models.OneToOneField(Donor, on_delete=models.CASCADE)
    BloodGroup = models.CharField(max_length=20)
    PackNo = models.CharField(max_length=20)
    RegDate = models.DateTimeField(auto_now_add=True)
    ExpDate = models.DateTimeField(max_length=10)
    QuantityOfBlood = models.CharField(max_length=4)    
