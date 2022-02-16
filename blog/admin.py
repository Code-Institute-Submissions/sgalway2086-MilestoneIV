from django.contrib import admin
from .models import Posts, Comment


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'poster',
        'post_title',
        'post_date',
        'body_text',
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'comment_body',
        'post_date',
        'post',
    )


admin.site.register(Posts, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
