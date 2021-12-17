from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('add_post/', views.add_post, name='add_post'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('view_post/<int:post_id>/', views.view_post, name='view_post')
]
