from django.shortcuts import render
from .models import Posts
import datetime

# Create your views here.


def blog(request):
    return render(request, 'blog/blog.html')



def add_post(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            post = Posts()
            post.poster = request.user
            post.body_text = request.POST.get('body_text')
            post.post_date = datetime.time()
            post.post_title = request.POST.get('post_title')
            post.save()
        else:
            messages.error(request, 'Can not post. Please log in')
        return render(request, 'blog/blog.html')

