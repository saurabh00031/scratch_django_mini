from .models import *
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = User
        fields = '__all__' 


class CriminalSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = criminalModel
        fields = '__all__' 

class CrimSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = crimModel
        fields = '__all__' 


