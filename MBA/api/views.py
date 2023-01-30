from .forms import UserFrom, ProfleForm, imgForm
from .models import Profile as ProfileModel
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password


def Login(request):
    error = False
    page = "login"
    form = UserFrom()
    if request.method == 'POST':
        username = request.POST.get("username")
        print(username)
        password = request.POST.get("password")
        print(password)
        try:
            user = User.objects.get(username=username)
        except Exception as Error:
            error = Error
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("home")

    context = context = {'page': page, "error": error}
    return render(request, "login.html", context=context)


def Register(request):
    page = "register"
    error = False
    form = UserFrom()
    if request.method == "POST":
        form = UserFrom(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(request.POST.get("password"))
            try:
                user.username = user.username.lower()
            except:
                ''
            user.save()
            login(request, user)
            return redirect("home")
        else:
            error = form.errors.as_ul
    context = context = {'page': page, 'error': error}
    return render(request, 'Login.html', context)


def Logout(request):
    logout(request)
    return render(request, 'index.html')


@login_required(login_url="login")
def Settings(request):
    error = False
    form = ProfileModel.objects.get(username=request.user)
    if request.method == 'POST':
        form = ProfileModel.objects.get(username=request.user)
        form.first_last = request.POST.get("last_name")
        form.first_name = request.POST.get("first_name")
        form.email = request.POST.get("email")
        form.profile_pic = request.POST.get("profile_pic")
        form.gender = request.POST.get("gender")
        form.birthday = request.POST.get("birthday")
        form.country = request.POST.get("country")
        form.passion = request.POST.get("passion")
        form.connection = request.POST.get("connection")
        form.looking = request.POST.get("looking")
        form.status = request.POST.get("status")
        form.save()
        return redirect('home')
    context = {"form": form, "error": error}

    return render(request, 'profile.html', context)
