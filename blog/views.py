from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Posts, Comment
import datetime
from django.contrib import messages


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


def view_post(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    comments = Comment.objects.all()
    context = {
        'post': post,
        'comments': comments,
    }
    return render(request, 'blog/view_post.html', context)


def add_comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Posts, pk=post_id)
        comments = Comment.objects.all()
        if request.user.is_authenticated:
            print(post)
            print(comments)
            comment = Comment()
            comment.user = request.user
            comment.comment_body = request.POST.get('comment_text')
            comment.post_date = datetime.time()
            comment.post = post_id
            comment.save()
            post = get_object_or_404(Posts, pk=post_id)
            comments = Comment.objects.all()
            context = {
                'post': post,
                'comments': comments,
            }
            return render(request, 'blog/view_post.html', context)
        else:
            post = get_object_or_404(Posts, pk=post_id)
            comments = Comment.objects.all()
            context = {
                'post': post,
                'comments': comments,
            }
            messages.error(request, 'Can not comment. Please log in')
        return render(request, 'blog/view_post.html', context)
    return render(request, 'blog/view_post.html', context)
