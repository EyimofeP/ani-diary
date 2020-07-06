from django.db import models
from django.contrib.auth.models import User

#Author Model
class Author(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	name = models.CharField(max_length=200, null=True)
	bio = models.TextField(null=True)
	instagram = models.CharField(max_length=50, null=True)
	phone = models.CharField(max_length=50, null=True)
	picture = models.ImageField(upload_to="authors/photos", null=True)
	date_joined = models.DateTimeField(auto_now_add =True)
	#Setting name for object
	def __str__(self):
		return self.name