

from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("login/",view=views.Login,name='login'),
        
]



