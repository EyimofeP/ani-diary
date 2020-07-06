from django.urls import path

#Import Views
from . import views

app_name = "blog"

urlpatterns = [
	#rhos.com
	path("",views.home, name="home"),
	#rhos.com/blog
	path("blog/",views.blog, name="blog"),
	#rhos.com/blog/hello-world/
	path("blog/article/",views.article, name="article"),
	#rhos.com/category
	path("category/",views.category, name="category"),
	#rhos.com/about-us
	path("about-us/",views.about, name="about"),
	#rhos.com/search
	path("search/",views.search, name="search"),
]