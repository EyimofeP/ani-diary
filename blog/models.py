from django.db import models
from django.utils import timezone #Importing Timezone

#Import Author Model
from author.models import Author

#Category DB
class Category(models.Model):
	name = models.CharField(max_length=200, null=True)
	description = models.TextField(max_length=200, null=True)
	picture = models.ImageField(upload_to="category/",null=True)

#Tags DB
class Tags(models.Model):
	name = models.CharField(max_length=200, null=True)

#Post DB
class Post(models.Model):
	author = models.ForeignKey(Author,on_delete=models.DO_NOTHING,null=True)
	title = models.CharField(max_length=200, null=True)
	short_description = models.TextField(max_length=200, null=True)
	date = models.DateTimeField(default=timezone.now)
	post_picture = models.ImageField(upload_to="posts/headers",null=True)
	slug = models.SlugField(max_length=100,null=True)
	category = models.ManyToManyField(Category)
	tags = models.ManyToManyField(Tags)


