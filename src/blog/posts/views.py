from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.utils import timezone
from .models import Post
from .forms import PostForm


class PostListView(ListView):
	model 				= Post
	paginate_by 		= 10
	def get_context_data(self ,**kwargs):
		context 		= super().get_context_data(**kwargs)
		context['now'] 	= timezone.now()
		
		return context
	


class PostDetailView(DetailView):
    model 				= Post

    def get_context_data(self, **kwargs):
        context 		= super().get_context_data(**kwargs)
        context['now'] 	= timezone.now()
        return context


class PostCreateView(CreateView):
	form_class 		=  PostForm
	template_name 	=  'posts/post_form.html'
	def form_valid(self, form):
		instance 		= form.save(commit=False)
		#instance.owner 	= self.request.user
		return super (PostCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context 			= super(PostCreateView, self).get_context_data(*args, **kwargs)
		context['title'] 	= 'NewPost'
		return context


class PostUpdateView(UpdateView):
	form_class 		= PostForm
	template_name 	= 'posts/detail-update.html'

	def get_queryset(self):
		return Post.objects.all()

	def form_valid(self, form):
		instance 		= form.save(commit=False)
		#instance.owner 	= self.request.user
		return super (PostUpdateView, self).form_valid(form)


	def get_context_data(self, *args, **kwargs):
		context 			= super(PostUpdateView, self).get_context_data(*args, **kwargs)
		context['title'] 	= 'PostUpdate'
		return context

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')
	