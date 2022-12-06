
from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login,authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.generic import CreateView
from django.contrib import messages
from .models import User as mu
from .models import *
from .decorators import *
import pyrebase
from rest_framework.response import Response
from .serializers import *


from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import HttpResponse





# home Page❤️. .............................................................................  #


def index(request):
    return render(request, 'index.html')


# registration of police❤️...............................................................................  #

class PoliceView(CreateView):
    model = User
    form_class = policeReg
    template_name = 'register_police.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'police'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'Police Station Data has been updated successfully!')
        login(self.request,user)
        return redirect("home")

# login of police❤️............................................................................... #

def sign_police(request):
    if request.method == "POST":
        # check if user has entered correct credientials
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_police == True:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, 'You are not authorized to access this page!')
        else:
            messages.error(request, 'Invalid Credentials!,plz try again')
            return redirect("sign_police")
    return render(request, 'sign_police.html')

# logout  of police❤️............................................................................... #


def letsout(request):
    logout(request)
    return render(request, 'index.html')



# page after signed in of police❤️............................................................................... #

def signpg_police(request):
    police_data = policeModel.objects.all()
    police = {
        "police_info": police_data
    }
    return render(request, 'signpg_police.html', police)

# update of police❤️ .............................................................................................#







@police_required
def update_police_data(request):
    this_police = policeModel.objects.get(user=request.user)
    police_inf = mu.objects.get(email=request.user.email)
    if request.method == "POST":
        station_name = request.POST.get('station_name')
        station_incharge = request.POST.get('station_incharge')
        station_city = request.POST.get('station_city')
        mobile = request.POST.get('mobile')
        email1 = request.POST.get('email1')
        email2 = request.POST.get('email2')
        email3 = request.POST.get('email3')
        email4 = request.POST.get('email4')


        this_police.station_name = station_name
        this_police.station_incharge = station_incharge
        this_police.station_city = station_city
        this_police.mobile = mobile 
        this_police.email1 = email1
        this_police.email2 = email2
        this_police.email3 = email3
        this_police.email4 = email4
        this_police.save()

        police_inf.email = email1
        police_inf.save()
        form=policeReg()
        messages.success(request, '...your data has been updated Successfully!')

    police_dat = {
        "police_info": this_police,
        "my_police_inf": police_inf
    }

    return render(request, 'edit_police.html', police_dat)


# addition of criminal detected data❤️ .......................................................................#


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def add_criminal(request):
    if request.method=='POST':
        fm=criminalReg(request.POST,request.FILES)
        print('all not kkk............')
        if fm.is_valid():
           print('all kkk........')
           fm.save()
           print('data saved..........')
           fm=criminalReg()
           stud=criminalModel.objects.all()
           messages.success(request, '...criminal data has been updated Successfully!')
           return redirect('home')
        else:
           print('some error !!!!!!!!!!!!!')
           messages.success(request, '...criminal data not been uploaded !')
           return render(request,'add_criminal.html')   
    else:
        fm=criminalReg()
        stud=criminalModel.objects.all()
        return render(request,'add_criminal.html',{'formx':fm,'stu':stud })



# show profile page of police station❤️.................................................................#

@police_required
def profile_police(request):
    print("inside the profile page function...........!")
    pol_data = policeModel.objects.get(user=request.user)
    print(pol_data)
    sp = {
        "sg" : pol_data
    }
    return render(request, 'profile_police.html', sp)



# show criminal data❤️.......................................................................#

def show_crim(request):
    crim_data = crimModel.objects.all()
    sp = {
        "stu": crim_data
    }
    return render(request, 'show_crim.html', sp)




# show the criminal data❤️.......................................................................#

def showdata(request,id):
    crim_data = crimModel.objects.get(crims_id=id)
    sp = {
        "stu": crim_data
    }
    return render(request, 'profile_crim.html', sp)


# def showdatax(request,id):
#     crim_data = crimModel.objects.get(pk=id)
#     sp = {
#         "stu": crim_data
#     }
#     return render(request, 'profile_crim.html', sp)


# update the criminal data❤️.......................................................................#

def updatedata(request,id):
    if request.method=='POST':
        pi=crimModel.objects.get(crims_id=id)
        fm=crimReg(request.POST,request.FILES,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'crim data re-updated successfully !')
    else:
        pi=crimModel.objects.get(crims_id=id)
        fm=crimReg(instance=pi)
    return render(request,'update_crim.html',{'formx':fm})



# delete the criminal data❤️.......................................................................#

def deletedata(request,id):
    if request.method=='POST':
        dlt=crimModel.objects.get(crims_id=id)
        dlt.delete()
        messages.success(request, '...criminal data deleted successfully !')
        return redirect('show_crim')
    


# search the criminal by crim_id❤️.......................................................................#

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        ctr = crimModel.objects.filter(crims_id__icontains=q)
    return render(request, 'search.html', {'ct': ctr})


# .........................................................................................................#


















####################################################################################


@api_view(['GET'])
def registerAPI(request):
    products = User.objects.all()
    serializer = UserSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)











######################################################################################################


@api_view(['GET'])
def criminalAPI(request):
    products = criminalModel.objects.all()
    serializer = CriminalSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def criminalDetailsAPI(request, id):
    product = get_object_or_404(criminalModel, crim_id=id)
    serializer =OrgSerializer(product, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)



######################################################################################################



@api_view(['GET'])
def orgAPI(request):
    products = orgModel.objects.all()
    serializer = OrgSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def orgDetailsAPI(request,id):
    products = orgModel.objects.get(name=id)
    serializer = OrgSerializer(products, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)









########################################################################################################

@api_view(['GET'])
def crimAPI(request):
    products = crimModel.objects.all()
    serializer = CrimSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def crimDetailsAPI(request,id):
    products = crimModel.objects.get(crims_id=id)
    serializer = CrimSerializer(products, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def editCrimAPI(request,id):
    
    product = get_object_or_404(crimModel, crims_id=id)
    serializer = CrimSerializer(product, data=request.data)

    if serializer.is_valid():

        crims_id = serializer.validated_data['crims_id']
        name = serializer.validated_data['name']

        # physical characteristics

        height = serializer.validated_data['height']
        eyes = serializer.validated_data['eyes']
        skin = serializer.validated_data['skin']


        # 4->3  3->2  2->1 shifting of locations for tracing locations............................
        
        # naye 4th mein koi change nahi and that is most updated location


        lat1 = product.lat2
        longt1 = product.longt2

        lat2 = product.lat3
        longt2 = product.longt3

        lat3 = product.lat4
        longt3 = product.longt4

        lat4 = serializer.validated_data['lat4']
        longt4 = serializer.validated_data['longt4']
        

        # 4->3  3->2  2->1 shifting of locations for tracing locations............................




        # image

        refer = serializer.validated_data['refer']

        # image
        
        sorrows=crimModel(crims_id=crims_id,name=name,height=height,eyes=eyes,skin=skin,lat1=lat1,longt1=longt1,lat2=lat2,longt2=longt2,lat3=lat3,longt3=longt3,lat4=lat4,longt4=longt4,refer=refer)
        sorrows.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)



        # serializer.data['lat3']=product.lat4
        # serializer.data['longt3']=product.longt4
        
        # serializer.data['lat2']=product.lat3
        # serializer.data['longt2']=product.longt3

        # serializer.data['lat1']=product.lat2
        # serializer.data['longt1']=product.longt2

        # serializer.data['lat4']= serializer.data['lat4']
        # serializer.data['longt4']=serializer.data['longt4']



@csrf_exempt 
def add_crim(request):
    if request.method=='POST':
        fm=crimReg(request.POST,request.FILES)
        print('all not kkk............')
        if fm.is_valid():
           print('all kkk........')
           fm.save()
           print('data saved..........')
           fm=crimReg()
           stud=crimModel.objects.all()
           messages.success(request, '...criminal data has been updated Successfully!')
           return redirect('home')
        else:
           print('some error !!!!!!!!!!!!!')
           messages.success(request, '...criminal data not been uploaded !')
           return render(request,'add_crim.html')   
    else:
        fm=crimReg()
        stud=crimModel.objects.all()
        return render(request,'add_crim.html',{'formx':fm,'stu':stud })


########################################################################################################