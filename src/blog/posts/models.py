from django.db import models
from django.db.models.signals import pre_save,post_save
from django.urls import reverse

from .utils import unique_slug_generator

class Post(models.Model):
	title 			= models.CharField(max_length=30)
	content 		= models.TextField()
	image 			= models.ImageField(null=True,
	 									blank=True,
	 									height_field='height_field',
	 									width_field='width_field'
	 									)
	height_field	= models.IntegerField(default=0)
	width_field		= models.IntegerField(default=0)
	updated			= models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp		= models.DateTimeField(auto_now=False,auto_now_add=True)
	slug			= models.SlugField(null=True,blank=True)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', args=[str(self.slug)])


	class Meta:
		ordering =['-updated', '-timestamp']



def s_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)




pre_save.connect(s_pre_save_receiver, sender=Post)