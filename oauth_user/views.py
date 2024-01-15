from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout


def index(request):
    if request.user.is_authenticated:
        context = {
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "email": request.user.email,
        }
        return render(request, "oauth_user/index.html", context)

    return HttpResponseRedirect("/login")


def login_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")

    return render(request, "oauth_user/login.html")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/login")
