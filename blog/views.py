from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from django.views.generic import ListView
from django.core.paginator import Paginator

from .models import Category, Post
from author.models import Author
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

#Category Display Page
def category(request,pk):
	category = get_object_or_404(Category,pk=pk)
	frontend = {
		"category":category,
	}
	return render(request,"blog/category-display.html",frontend)

#Author Display Page
def author(request,username):
	authors = get_object_or_404(Author,author__username=username)
	frontend = {
		"author":authors,
	}
	return render(request,"blog/about.html",frontend)

def about(request):
	authors = Author.objects.all()

	frontend = {
		"authors":authors,
	}
	return render(request,"blog/about-us.html",frontend)
	
