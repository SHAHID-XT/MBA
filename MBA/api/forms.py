from django.forms import ModelForm
from .models import Recharge, Rooms, Message, Like, Match, Profile, img
from django.contrib.auth.models import User


class RoomForm(ModelForm):
    class Meta:
        model = Rooms
        fields = '__all__'
        exclude = ['host', 'participants']


class imgForm(ModelForm):
    class Meta:
        model = img
        fields = ['img',"user"]


class UserFrom(ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        # fields = '__all__'


class ProfleForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
