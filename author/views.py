from django.shortcuts import render, redirect

from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import *
from .decorators import *

from .models import Author
from blog.models import *

#Register a User
@unauthenticated_user   #Redirects unregisted user to login page
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
@unauthenticated_user
def signIn(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request,username=username,password=password)
		if user is not None:
			login(request, user)
			return redirect("author:profile")
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
	post = Post.objects.filter(author=request.user.author)
	count = post.count()#Counting Number of Post Per Author

	frontend = {
		"count":count,
		"posts":post,
	}
	return render(request, "author/admin.html",frontend)

#UserProfileSettings
@login_required(login_url="author:login")
@admin_only
def userProfile(request):
	author = request.user.author
	form = AuthorForm(instance=author)
	frontend = {"form":form}

	if request.method == "POST":
		form = AuthorForm(request.POST, request.FILES, instance=author)
		if form.is_valid:
			form.save()
	return render(request,"author/settings.html",frontend)

#Create A New Blog Post
class PostCreate(CreateView):
	model = Post
	form_class = PostForm
	template_name = "author/create-post.html"

	def form_valid(self,form):
		form.instance.author = self.request.user.author
		return super().form_valid(form)

#Update Blog Post
class PostUpdate(UpdateView):
	model = Post
	form_class = PostForm
	template_name = "author/update-post.html"

#Delete Blog Post
class PostDelete(DeleteView):
	model = Post
	success_url = reverse_lazy("author:profile")


class CategoryCreate(CreateView):
	model = Category
	form_class = CategoryForm
	template_name = "author/create-category.html"

#Update Category
class CategoryUpdate(UpdateView):
	model = Category
	form_class = CategoryForm
	template_name = "author/update-category.html"

#Delete Category
class CategoryDelete(DeleteView):
	model = Category
	success_url = reverse_lazy("author:profile")

class TagCreate(CreateView):
	model = Tag
	fields = "__all__"
	template_name = "author/create-tag.html"
