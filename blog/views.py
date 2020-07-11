from django.shortcuts import render
from django.http import HttpResponse

from .models import Post,Category
#Home Page
def home(request):
	posts = Post.objects.order_by("-date")[:3]
	category = Category.objects.all()

	frontend = {
		"posts" : posts,
		"category" : category,
	}
	return render(request,"blog/home.html", frontend)

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
