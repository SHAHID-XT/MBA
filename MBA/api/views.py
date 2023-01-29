from django.shortcuts import render
from .forms import UserFrom


def Login(request):
    page = "login"
    form = UserFrom()
    context = context = {'page': page}
    return render(request, "login.html", context=context)
# Create your views here.
