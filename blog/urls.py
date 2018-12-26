from django.urls import path

from .views import *


urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/<str:slug>/', post_datayl, name='post_datayl_url'),
    path('tags', tags_list, name='tags_list_url'),
    path('tag/<str:slug>/', tag_datayl, name='tag_datayl_views'),
]