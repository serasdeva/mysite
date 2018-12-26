from django.urls import path

from .views import posts_list, post_datayl


urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/<str:slug>/', post_datayl, name='post_datayl_url'),
]