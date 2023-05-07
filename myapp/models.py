from django.db import models
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length = 10, verbose_name = 'タグ')
    author = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 15, verbose_name = 'タイトル')
    content = models.CharField(max_length = 140, verbose_name = '投稿内容')
    author = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
    )
    tag = models.ForeignKey(
        Tag,
        on_delete = models.PROTECT,
    )
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('myapp:detail', kwargs={'pk': self.pk})
