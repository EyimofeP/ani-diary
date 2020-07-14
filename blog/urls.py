from django.urls import path

#Import Views
from . import views

app_name = "blog"

urlpatterns = [
	#rhos.com
	path("",views.Home.as_view(), name="home"),
	#rhos.com/blog
	path("blog/",views.blog, name="blog"),
	#rhos.com/blog/hello-world/
	path("blog/article/<int:pk>/<slug:slug>/",views.article, name="article"),
	#rhos.com/category
	path("category/",views.categoryPage, name="category"),
	#rhos.com/category/23/
	path("category/<pk>/",views.category, name="category-page"),
	#rhos.com/about-us
	path("about-us/",views.about, name="about-page"),
	#rhos.com/about-us/@2/
	path("about-us/@<username>/",views.author, name="about"),
]