from django.contrib import admin

# Register your models here.

from .models import PostModel


class PostModelAdmin(admin.ModelAdmin):
	fields = [
	'title',
	'slug',
	'content',
	'publish',
	'publish_date',
	'active',
	'updated',
	'timestamp',
	'get_age',
	]
	readonly_fields = ['updated' ,'timestamp', 'get_age']
	
	def new_content(self, obj, *arg, **kwargs):
		return str(obj.title)

	def get_age(self, obj, *arg, **kwargs):
		return str(obj.age)

	class Meta:
		model = PostModel
	

admin.site.register(PostModel, PostModelAdmin)