from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.files import ImageField
import uuid


class User(AbstractUser):      
    is_police = models.BooleanField(default=False)
    is_criminal= models.BooleanField(default=False)


class policeModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    station_name = models.CharField(max_length=50)
    station_incharge = models.CharField(max_length=50)
    station_city = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    email1 = models.CharField(max_length=50)
    email2 = models.CharField(max_length=50)
    email3 = models.CharField(max_length=50)
    email4 = models.CharField(max_length=50)

    def __str__(self):
        return self.station_name


class criminalModel(models.Model):
    crim_id=models.CharField(max_length=50,blank=False, null=False,unique=True)
    name=models.CharField(max_length=50)
    height = models.FloatField(null=True, blank=True)
    eyes=models.CharField(max_length=20)
    skin=models.CharField(max_length=20)
    lat=models.CharField(max_length=20)
    longt=models.CharField(max_length=20)
    age=models.IntegerField(blank=True, null=True)
    org = models.ImageField(upload_to ='media/') #original image

    def __str__(self):
        return self.name

class crimModel(models.Model):
    crims_id=models.CharField(max_length=50,primary_key=True)

    name=models.CharField(max_length=50)
    height = models.FloatField(null=True, blank=True)
    eyes=models.CharField(max_length=20)
    skin=models.CharField(max_length=20)

    lat1=models.CharField(max_length=20)
    longt1=models.CharField(max_length=20)
    lat2=models.CharField(max_length=20)
    longt2=models.CharField(max_length=20)
    lat3=models.CharField(max_length=20)
    longt3=models.CharField(max_length=20)
    lat4=models.CharField(max_length=20)
    longt4=models.CharField(max_length=20)
    refer = models.ImageField(upload_to ='media/')

    def _str_(self):
        return self.name