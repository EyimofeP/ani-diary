from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from django.views.generic import ListView
from django.core.paginator import Paginator

from .models import Category, Post
#Home Page
class Home(ListView):
	template_name = "blog/home.html"
	context_object_name = "posts"

	def get_queryset(self):
		return Post.objects.order_by("-date")[:3]

#All Blog Page
def blog(request):
	posts = Post.objects.order_by("-date")
	paginator = Paginator(posts,6)
	page = request.GET.get('page')
	paged_posts = paginator.get_page(page)  

	frontend = {
		"posts":paged_posts,
	}
	return render(request,"blog/blog.html",frontend)

#Article page
def article(request, pk):
	article = get_object_or_404(Post,pk=pk)
	trends = Post.objects.order_by("-date")[:3]
	frontend = {
		"trends":trends,
		"article":article,
	}
	return render(request,"blog/article.html",frontend)

#Category Page
def categoryPage(request):
	category = Category.objects.all()

	frontend = {
		"categories":category,
	}
	return render(request,"blog/category.html",frontend)
"""
class Category(ListView):
	template_name = "blog/category.html"
	context_object_name = "categories"

	def get_queryset(self):
		category = 
		return category"""

#About Page
def about(request):
	return HttpResponse("About")

#Search Page
def search(request):
	return HttpResponse("Search")
