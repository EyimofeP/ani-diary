from django.contrib import admin

#Import Models
from .models import Author

#Organizing Author Admin
class AuthorAdmin(admin.ModelAdmin):
	list_display = ("name", "instagram","phone")
	search_fields = ("name","instagram")

#Registering model
admin.site.register(Author,AuthorAdmin)
