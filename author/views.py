from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

from .forms import *
from .decorators import *

#Register a User
@login_required(login_url="author:login")   #Redirects unregisted user to login page
@admin_only
def register(request):
	form = UserForm()
	if request.method == "POST":
		user = UserForm(request.POST)
		if user.is_valid():
			user.save()
			return redirect("author:login")
	frontend = {"form":form}
	return render(request, "author/register.html",frontend)

#Log in a User
@login_required(login_url="author:login")   #Redirects unregisted user to login page
@admin_only
def signIn(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request,username=username,password=password)
		if user is not None:
			login(request, user)
			return redirect("/")
		else:
			return redirect("author:login")
	return render(request, "author/login.html")

#Logout a User
def signOut(request):
	if request.method == "POST":
		logout(request)
		return redirect("/")

#User Profile
@login_required(login_url="author:login")
@admin_only
def userAdmin(request):
	return HttpResponse("Profile")
"""
#UserProfileSettings
def userProfile(request):
	if request.method == "POST"""