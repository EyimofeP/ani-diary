from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User 

from .models import Author
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
	class Meta:
		model = Author
		fields = "__all__"
		exclude = ["author"]