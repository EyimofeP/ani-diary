from django.shortcuts import render
from django.http import HttpResponse

#Home Page
def home(request):
	return HttpResponse("Home")

#All Blog Page
def blog(request):
	return HttpResponse("Blog")

#Article page
def article(request):
	return HttpResponse("Article")

#Category Page
def category(request):
	return HttpResponse("Category")

#About Page
def about(request):
	return HttpResponse("About")

#Search Page
def search(request):
	return HttpResponse("Search")
