from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s)
    return new_slug + '-' + str(int(time()))



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200, db_index = True)
    slug = models.SlugField(max_length=150, blank=True, unique = True)
    body = models.TextField(blank=True, db_index=True)
    date = models.DateField(auto_now_add=True)
    tag = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def get_absolute_url(self):
        return reverse('post_datayl_url', kwargs={'slug':self.slug})


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title


class Tag(models.Model):
	title = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50, unique=True)

	def get_absolute_url(self):
		return reverse('tag_datayl_views', kwargs={'slug':self.slug})

	def __str__(self):
		return self.title