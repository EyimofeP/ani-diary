from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User 

from froala_editor.widgets import FroalaEditor

from .models import Author
from blog.models import Post,Category

class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email","password1","password2"]
		help_texts = {
			"username": "Username should be more than 30 characters",
			"email": "Do not share your e-mail with anyone!",
			"first_name": "Enter your First Name",
			"last_name": "Enter your Last Name",
		}

class AuthorForm(ModelForm):
	picture = forms.ImageField(label="Profile Avatar:", required=False,widget=forms.FileInput)
	class Meta:
		model = Author
		fields = "__all__"
		exclude = ["author"]

class PostForm(ModelForm):
	post_picture = forms.ImageField(label="Main Photo (Optional):", required=False,widget=forms.FileInput)
	title = forms.CharField(label="Title of Blog")
	short_description = forms.CharField(label="A Brief Description about the Blog e.g 'Boy Trauma'",widget=forms.Textarea)
	main_content = forms.CharField(label="Main Content of The Blog",widget=FroalaEditor)
	slug = forms.SlugField(label="Url of Blog e.g 'my-first-blog'")
	#date = forms.DateTimeField(required=False)

	class Meta:
		model = Post
		fields = ['title','short_description','main_content','post_picture','slug','category','tags']

class CategoryForm(ModelForm):
	picture = forms.ImageField(label="Category Photo (Optional):", required=False,widget=forms.FileInput)
	class Meta:
		model = Category
		fields = "__all__"