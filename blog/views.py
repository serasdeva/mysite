from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def posts_list(request):
	title = "Posts list"
	posts  = Post.objects.all()
	return render(request, 'blog/index.html', context={'posts': posts, 'title': title})

def post_datayl(request, slug):
	post = Post.objects.get(slug__iexact=slug)
	return render(request, 'blog/post_datayl.html', context={'post': post})