from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('post/ajax/post', views.uploadPost, name = 'upload_post'),
]
