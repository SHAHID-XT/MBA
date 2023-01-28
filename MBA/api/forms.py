from django.forms import ModelForm
from .models import Recharge,Rooms,Message,Like,Match
from django.contrib.auth.models import User


class RoomForm(ModelForm):
    class Meta:
        model = Rooms
        fields = '__all__'
        exclude= ['host' ,'participants']
        
        
class UserFrom(ModelForm):
    class Meta:
        model = User
        fields =  ['username','email' ,'first_name' ,'last_name','gender']
        
        