from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='posts/', default='posts/default.jpg')
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='created_at')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')], default='published')
    objects = models.Manager()
    post_objects = PostObjects()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        if self.parent:
            return f'{self.author} replied to {self.parent.author} on {self.post}'
        else:
            return f'Comment by {self.author} on {self.post}'
    
    def clean(self):
        if self.parent and self.parent.post != self.post:
            raise ValidationError("Parent comment must be on the same post.")

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'author',)
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.author} likes {self.post}'