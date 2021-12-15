from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='post_search'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('post_create/', views.post_create, name='post_create'),
]
