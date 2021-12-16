from django.contrib import admin
from .models import Posts


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'poster',
        'post_title',
        'post_date',
        'body_text',
    )
admin.site.register(Posts, BlogAdmin)

