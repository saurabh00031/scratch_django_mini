from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import *



class policeReg(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email=forms.CharField(required=True ,widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta(UserCreationForm):
            model=User
            fields=['username','email','password1','password2']
            labels={'email':'Email'}
            widgets={'username':forms.TextInput(attrs={'class':'form-control'})}



    #   class policeReg(UserCreationForm):
    # email = forms.EmailField(required=True)
    # password = forms.PasswordInput()

    # class Meta(UserCreationForm):
    #     model=User
    #     fields = ['id','email','username'] 
        
        
      
        
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_police = True
        user.save()
        plc = policeModel.objects.create(user=user)
        return user




class criminalReg(forms.ModelForm):
    class Meta:
        model=criminalModel
        fields= ['crim_id','name','height','eyes','skin','age','org'] 
        widgets={
            'crim_id':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'height':forms.TextInput(attrs={'class':'form-control'}),
            'eyes':forms.TextInput(attrs={'class':'form-control'}),
            'skin':forms.TextInput(attrs={'class':'form-control'}),
            # 'lat':forms.TextInput(attrs={'class':'form-control'}),
            # 'longt':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'org':forms.FileInput(attrs={'class':'form-control'}),
        }
        
class crimReg(forms.ModelForm):
    class Meta:
        model=crimModel
        fields= '__all__' 
        widgets={
            'crims_id':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'height':forms.TextInput(attrs={'class':'form-control'}),
            'eyes':forms.TextInput(attrs={'class':'form-control'}),
            'skin':forms.TextInput(attrs={'class':'form-control'}),
            'lat1':forms.TextInput(attrs={'class':'form-control'}),
            'longt1':forms.TextInput(attrs={'class':'form-control'}),
            'lat2':forms.TextInput(attrs={'class':'form-control'}),
            'longt2':forms.TextInput(attrs={'class':'form-control'}),
            'lat3':forms.TextInput(attrs={'class':'form-control'}),
            'longt3':forms.TextInput(attrs={'class':'form-control'}),
            'lat4':forms.TextInput(attrs={'class':'form-control'}),
            'longt4':forms.TextInput(attrs={'class':'form-control'}),
            'refer':forms.FileInput(attrs={'class':'form-control'}),
           
        }

        