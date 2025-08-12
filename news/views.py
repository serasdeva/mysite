from django.shortcuts import render, get_object_or_404, redirect

from .models import News, Category
from .forms import NewsForm

# Create your views here.

def index(request):
	news = News.objects.select_related('category').all()
	context = {
		'news': news,
		'title': 'Список новостей',
	}
	return render(request, 'news/index.html', context)


def get_category(request, category_id):
	news = News.objects.filter(category_id=category_id).select_related('category')
	category = get_object_or_404(Category, pk=category_id)
	return render(request, 'news/category.html', {'news': news, 'category': category})


def view_news(request, news_id):
	#news_item = News.objects.get(pk=news_id)
	news_item = get_object_or_404(News, pk=news_id)
	return render(request, 'news/view_news.html', {'news_item': news_item})


def add_news(request):
	if request.method=='POST':
		form = NewsForm(request.POST, request.FILES)
		if form.is_valid():
			news = form.save()
			return redirect(news)
	else:
		form = NewsForm()
	return render(request, 'news/add_news.html', {'form': form})