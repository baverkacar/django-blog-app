from article.views import index
from django.shortcuts import render,redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate, logout
from django.contrib import messages 

# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None) 
    if form.is_valid(): 
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        login(request, newUser)
        messages.error(request,"Logined successfully")
        return redirect("index") 
    context = {
        "form": form
    } 
    return render(request, "register.html", context)


def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request,"Username or password is wrong")
            return render("login", context)
        else:
            messages.success(request, "Logined successfully")
            login(request, user)
            return redirect("index")
    return render(request, "login.html", context)


def logoutUser(request):
    logout(request)
    messages.success(request, "Successfully Logout")
    return redirect("index")