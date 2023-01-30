

from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("login/",view=views.Login,name='login'),
    path("register/",view=views.Register,name='register'),
    path("logout/",view=views.Logout,name='logout'),
    path("setting/",view=views.Settings,name="setting"),
    path("members/",view=views.Members,name="members"),
        
]



