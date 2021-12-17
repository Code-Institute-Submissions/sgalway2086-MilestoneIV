from django.db import models

# Create your models here.
class Posts(models.Model):
    poster = models.CharField(max_length=254, null=False, blank=False)
    post_title = models.CharField(max_length=80, null=True, blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    body_text = models.TextField()


    def __str__(self):
        return self.name
