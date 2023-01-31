from .forms import UserFrom, ProfleForm, imgForm
from .models import Profile as ProfileModel
from .models import img as imgModel
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password


def Home(request):
    users = ProfileModel.objects.all()[0:4]
    for usere in users:
        try:
            usere.img = imgModel.objects.get(user=usere.username)
        except:
            ""
        try:
            usere.age = 2023 - int(usere.birthday.split("-")[0])
        except:
            ''
    context = context = {'users': users}
    return render(request, "index.html", context)


def Login(request):
    error = False
    page = "login"
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
        except Exception as Error:
            error = Error
        user = authenticate(request, username=username, password=password)
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
    context = {'page': page, 'error': error}
    return render(request, 'Login.html', context)


def Logout(request):
    logout(request)
    return render(request, 'index.html')


@login_required(login_url="login")
def Settings(request):
    error = False
    actualimg = False
    mform = False
    try:
        mform = ProfileModel.objects.get(username=request.user.username)
    except:
        ""
    try:
        actualimg = imgModel.objects.get(user=request.user.username)
    except:
        ""
    try:
        email = mform.email
    except:
        ""

    if request.method == "POST":
        isoldfound = False
        try:
            old_image = imgModel.objects.get(user=request.user)
            isoldfound = True
        except:
            ""

        if isoldfound:
            imguser = imgForm(request.POST, request.FILES, instance=old_image)
        else:
            imguser = imgForm(request.POST, request.FILES)
        if imguser.is_valid():
            imguser.save()
        else:
            print(imguser.errors.as_text)

    if request.method == 'POST':
        form = ProfileModel.objects.get(username=request.user)
        email = form.email
        forms = ProfleForm(request.POST, instance=form)
        if forms.is_valid():
            forms.save()
            form.email = email
            print(request.POST.get("country"))
            form.country = request.POST.get("country")
            form.save()
        else:
            print(forms.errors.as_text)
        return redirect('home')
    context = {"form": mform, "error": error, "profilep": actualimg}

    return render(request, 'profile.html', context)


def Members(request):
    memmers = ProfileModel.objects.all()[0:20]
    context = {"memmers": memmers}
    for user in memmers:
        try:
            user.age = 2023 - int(user.birthday.split("-")[0])
        except:
            ''
        try:
            user.img = imgModel.objects.get(user=user.username)
        except Exception as e:
            pass
    return render(request, 'members.html', context)



def ProfilePage(request, q):
    user = False
    try:
        user = ProfileModel.objects.get(username=q)
    except Exception as D:
        print(D)
        ""

    try:
        img = imgModel.objects.get(user=q)
        user.img = img
    except:
        ""
    context = {"user": user}
    return render(request, 'profilepage.html', context)
