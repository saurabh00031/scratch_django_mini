from django.urls import path
from CRapp import views
from django.contrib.auth import views as auth_views


urlpatterns = [


    # $ection : Others ❤️

    # url for homepage ................................................................................#
    path('',views.index,name="home"), 



    # $ection for police ❤️

    # url for police registration ......................................................................#
    path('register_police/', views.PoliceView.as_view(), name="register_police"),
    # url for police login .......................................................................#
    path('sign_police/', views.sign_police, name="sign_police"),
    # url for police logout .......................................................................#
    path('letsout/', views.letsout, name="letsout"),
    #url for page after police sign in .....................................................................#.
    path('signpg_police/', views.signpg_police, name="signpg_police"),
    # url for profile page of police station................................................................#.
    path('profile_police/', views.profile_police, name="profile_police"),
    # url for police data updation .....................................................................#
    path("update_police_data/", views.update_police_data, name="update_police_data"),

    path('api/register', views.registerAPI, name="registerAPI"),
 
    path('api/org', views.orgAPI, name="orgAPI"),
    path('api/org/<id>/', views.orgDetailsAPI, name="orgDetailsAPI"),

    path('api/criminal', views.criminalAPI, name="criminalAPI"),
    path('api/criminal/<id>/', views.criminalDetailsAPI, name="criminalDetailsAPI"),
    
   

    path('api/crim', views.crimAPI, name="crimAPI"),
    path('api/crim/<id>/', views.crimDetailsAPI, name="crimDetailsAPI"),
    path('api/crim/edit/<id>/', views.editCrimAPI, name="editCrimAPI"),
    path('add_crim/',views.add_crim,name="add_crim"),
    # path('crim/edit/<id>/', views.crimEdit, name="crimEdit"),


   
     # $ection for criminal ❤️

    # url for criminal adding.................................................................................#
    path('add_criminal/',views.add_criminal,name="add_criminal"),
    # url for criminal data.................................................................................#
    #path('show_criminal/',views.show_criminal,name="show_criminal"),
    path('show_crim/',views.show_crim,name="show_crim"),
    # url for delete the criminal data...................................................................#
    path('delete/<id>/',views.deletedata,name="deletedata"),
    # url for updating the criminal data.......................................................................#
    path('update/<id>/',views.updatedata,name="updatedata"),
    # url for showing the criminal data.......................................................................#
    path('show/<id>/',views.showdata,name="showdata"),
    # path('showx/<int:id>/',views.showdatax,name="showdatax"),
    # url for searching in criminal data.......................................................................#
    path('search/', views.search, name="search"),





]