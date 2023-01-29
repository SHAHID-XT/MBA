from django.forms import ModelForm
from .models import Recharge,Rooms,Message,Like,Match,Profile
from django.contrib.auth.models import User


class RoomForm(ModelForm):
    class Meta:
        model = Rooms
        fields = '__all__'
        exclude= ['host' ,'participants']
        
        
class UserFrom(ModelForm):
    class Meta:
        model = Profile
        # fields =  ['username','email' ,'first_name' ,'last_name']
        fields = '__all__'

        
        