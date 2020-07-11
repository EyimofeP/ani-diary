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

#Registering model
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
