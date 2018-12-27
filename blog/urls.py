<<<<<<< HEAD
from django.urls import path

from .views import *


urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_datayl_url'),
    path('tags', tags_list, name='tags_list_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_datayl_views'),
=======
from django.urls import path

from .views import *


urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/<str:slug>/', post_datayl, name='post_datayl_url'),
    path('tags', tags_list, name='tags_list_url'),
    path('tag/<str:slug>/', tag_datayl, name='tag_datayl_views'),
>>>>>>> 9690f4cfcd0eae61a041a7d20aad8c587c487554
]