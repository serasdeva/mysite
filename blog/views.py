from django.shortcuts import render
from django.http import HttpResponse
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