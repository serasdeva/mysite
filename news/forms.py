from django import forms

from .models import Category, News


class NewsForm(forms.ModelForm):
	is_published = forms.BooleanField(label='Опубликовать', initial=True, required=False)

	class Meta:
		model = News
		fields = ['title', 'content', 'is_published', 'category', 'photo']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
			'category': forms.Select(attrs={'class': 'form-control'}),
		}