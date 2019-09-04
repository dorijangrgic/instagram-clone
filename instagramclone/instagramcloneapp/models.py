from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


def user_post_path(instance, filename):
    return 'posts/user_{0}/{1}'.format(instance.author.id, filename)


class Post(models.Model):
    image = models.ImageField(upload_to=user_post_path)
    description = models.TextField(max_length=300, null=True, blank=True)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
