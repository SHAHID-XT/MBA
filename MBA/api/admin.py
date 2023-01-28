from django.contrib import admin
from .models import Recharge,Rooms,Message,Like,Match,Profile

admin.site.register(Recharge)
admin.site.register(Rooms)
admin.site.register(Message)
admin.site.register(Match)
admin.site.register(Like)
admin.site.register(Profile)

# Register your models here.