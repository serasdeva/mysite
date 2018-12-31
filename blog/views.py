from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Tag
from .utils import *
from .forms import TagForm, PostForm

# Create your views here.
def login(request):
	return render(request, 'blog/login.html')

def posts_list(request):
	title = "Posts list"
	posts  = Post.objects.all()
	return render(request, 'blog/base_blog.html', context={'posts': posts, 'title': title})

def tags_list(request):
	tags = Tag.objects.all()
	return render(request, 'blog/tags_list.html', context={'tags': tags})


class PostDetail(ObjectDetailMixin, View):
	model = Post
	template = 'blog/post_datayl.html'


class TagDetail(ObjectDetailMixin, View):
	model = Tag
	template = 'blog/tag_datayl.html'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
	model_form = PostForm
	template = 'blog/post_create_form.html'
	raise_exception = True


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
	model_form = TagForm
	template = 'blog/tag_create.html'
	raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
	model = Post
	model_form = PostForm
	template = 'blog/post_update_form.html'
	raise_exception = True
	

class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
	model = Post
	template = 'blog/post_delete_form.html'
	redirect_url = 'posts_list_url'
	raise_exception = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
	model = Tag
	model_form = TagForm
	template = 'blog/tag_update_form.html'
	raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
	model = Tag
	template = 'blog/tag_delete_form.html'
	redirect_url = 'tags_list_url'
	raise_exception = True

