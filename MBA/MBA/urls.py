
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",view=views.Home,name="home"),
    path("login/",view=views.Login,name='login'),
]

