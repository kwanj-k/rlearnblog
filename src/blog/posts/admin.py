from django.contrib import admin
from .models import Post
#model admin
# Register your models here.


class PostModelAdmin(admin.ModelAdmin):
	list_display 		= ['title','timestamp','updated']
	list_display_links	= ['title']
	search_fields 	= ['title','content']

	class Meta:
		model = Post
			

admin.site.register(Post, PostModelAdmin)
