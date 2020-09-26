from django.shortcuts import render, redirect

from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

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
			username = user.cleaned_data['username']
			messages.success(request,f"Welcome New Author {username}")
			return redirect("author:login")
		else:
			for msg in user.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")
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
			messages.success(request, f"Welcome to your Dashboard @{username}")
			return redirect("author:profile")
		else:
			messages.error(request,"Invalid Credentials")
			return redirect("author:login")
	return render(request, "author/login.html")

#Logout a User
def signOut(request):
	if request.method == "POST":
		logout(request)
		messages.error(request,"Successfully Logged Out, Hope to see you soon!!!")
		return redirect("author:login")

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
			messages.success(request,f"Your Profile was successfully updated, {author.author.first_name}")
	return render(request,"author/settings.html",frontend)

#Create A New Blog Post
class PostCreate(SuccessMessageMixin,CreateView):
	model = Post
	form_class = PostForm
	template_name = "author/create-post.html"
	success_message = "Secret was successfully created"

	def form_valid(self,form):
		form.instance.author = self.request.user.author
		return super().form_valid(form)

#Update Blog Post
class PostUpdate(SuccessMessageMixin,UpdateView):
	model = Post
	form_class = PostForm
	template_name = "author/update-post.html"
	success_message = "Secret was successfully updated"


#Delete Blog Post
class PostDelete(SuccessMessageMixin,DeleteView):
	model = Post
	success_url = reverse_lazy("author:profile")
	success_message = "Secret was successfully disposed"


class CategoryCreate(SuccessMessageMixin,CreateView):
	model = Category
	form_class = CategoryForm
	template_name = "author/create-category.html"
	success_message = "Category was successfully updated"
"""
#Update Category
class CategoryUpdate(SuccessMessageMixin,UpdateView):
	model = Category
	form_class = CategoryForm
	template_name = "author/update-category.html"
	success_message = "Category was successfully updated"

#Delete Category
class CategoryDelete(DeleteView):
	model = Category
	success_url = reverse_lazy("author:profile")
"""
#Create Tag
class TagCreate(CreateView):
	model = Tag
	fields = "__all__"
	template_name = "author/create-tag.html"
