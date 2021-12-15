from django.views import generic
from .models import Post
from django.shortcuts import render

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created')
    template_name = 'post_search.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def post_create(request):
    return render(request, 'post_create.html')
