<<<<<<< HEAD
from django.shortcuts import redirect, render, get_object_or_404

from django.views.generic import View

from .models import Post, Tag
from .utils import ObjectDetailMixin
from .forms import TagForm

# Create your views here.
def posts_list(request):
	title = "Posts list"
	posts  = Post.objects.all()
	return render(request, 'blog/index.html', context={'posts': posts, 'title': title})

def tags_list(request):
	tags = Tag.objects.all()
	return render(request, 'blog/tags_list.html', context={'tags': tags})


class PostDetail(ObjectDetailMixin, View):
	model = Post
	template = 'blog/post_datayl.html'


class TagDetail(ObjectDetailMixin, View):
	model = Tag
	template = 'blog/tag_datayl.html'


class TagCreate(View):
	def get(self, request):
		form = TagForm()
		return render(request, 'blog/tag_create.html', context={'form': form})

	def post(self, request):
		bound_form = TagForm(request.POST)
		
		if bound_form.is_valid():
			new_tag = bound_form.save()
			return redirect(new_tag)

		return render(request, 'blog/tag_create.html', context={'form': bound_form})
=======
from django.shortcuts import render
from .models import Post, Tag

# Create your views here.
def posts_list(request):
	title = "Posts list"
	posts  = Post.objects.all()
	return render(request, 'blog/index.html', context={'posts': posts, 'title': title})

def post_datayl(request, slug):
	post = Post.objects.get(slug__iexact=slug)
	return render(request, 'blog/post_datayl.html', context={'post': post})

def tags_list(request):
	tags = Tag.objects.all()
	return render(request, 'blog/tags_list.html', context={'tags': tags})


def tag_datayl(request, slug):
	tag = Tag.objects.get(slug__iexact=slug)
	return render(request, 'blog/tag_datayl.html', context={'tag': tag})
>>>>>>> 9690f4cfcd0eae61a041a7d20aad8c587c487554
