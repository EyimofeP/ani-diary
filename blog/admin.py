from django.contrib import admin

#Import Models
from .models import *

#Organizing Post Admin
class PostAdmin(admin.ModelAdmin):
	list_display = ("id","author", "title","date","slug")
	search_fields = ("title",)
	list_display_links = ("author",)
	list_filter = ("author","category","tags")
	list_per_page = 25

class CommentAdmin(admin.ModelAdmin):
	list_display = ("id","name", "post","email","active")
	search_fields = ("body",)
	list_display_links = ("name","email",)
	list_editable = ('active' ,)
	list_filter = ("active","name","post")
	list_per_page = 35
	actions = ['approve_comment']

	def approve_comment(self,request, queryset):
		queryset.update(active=True)

#Registering model
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)
 