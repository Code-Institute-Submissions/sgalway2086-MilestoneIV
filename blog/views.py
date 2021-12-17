from django.shortcuts import render, redirect, reverse
from .models import Posts
import datetime
from django.contrib import messages

# Create your views here.


def blog(request):
    posts = Posts.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/blog.html', context)



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
        return redirect(reverse('blog'))
