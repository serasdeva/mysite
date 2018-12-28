from django.shortcuts import redirect, render, get_object_or_404

from django.views.generic import View

from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin
from .forms import TagForm, PostForm

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


class PostCreate(ObjectCreateMixin, View):
	model_form = PostForm
	template = 'blog/post_create_form.html'


class TagCreate(ObjectCreateMixin, View):
	model_form = TagForm
	template = 'blog/tag_create.html'
