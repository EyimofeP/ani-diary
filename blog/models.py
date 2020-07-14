from django.db import models
from django.utils import timezone #Importing Timezone
from django.urls import reverse

from froala_editor.fields import FroalaField

#Import Author Model
from author.models import Author

#Category DB
class Category(models.Model):
	name = models.CharField(max_length=200, null=True)
	description = models.TextField(max_length=200, null=True)
	picture = models.ImageField(upload_to="category/",null=True, default="category/default.jpg")
	
	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("author:create-category")


#Tags DB
class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)
	
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("author:create-tag")
 
#Post DB
class Post(models.Model): 
	author = models.ForeignKey(Author,on_delete=models.DO_NOTHING,null=True)
	title = models.CharField(max_length=200, null=True)
	short_description = models.TextField(max_length=200, null=True)
	main_content = FroalaField(null=True)
	date = models.DateTimeField(default=timezone.now)
	post_picture = models.ImageField(upload_to="posts/headers",null=True, default="authors/default.jpeg")
	slug = models.SlugField(max_length=100,null=True)
	category = models.ManyToManyField(Category,blank=True,verbose_name="Category/Genre (Optional) e.g Love,Drama,HeartBreaking..")
	tags = models.ManyToManyField(Tag,blank=True,verbose_name="Tags/Emotions (Optional)  e.g Sad,Happy, Funny")

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("author:profile")

class Comment(models.Model):
	post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments",null=True)
	name = models.CharField(max_length=200, null=True)
	email = models.EmailField(null=True)
	body = models.TextField(null=True)
	created = models.DateTimeField(auto_now_add=True,null=True)
	active = models.BooleanField(default=True,null=True)

	class Meta:
		ordering = ['created']

	def __str__(self):
		return f"Comment by {self.name}"