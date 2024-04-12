from rest_framework import serializers
from blog.models import Post, Category
from django.conf import settings

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id', 'title', 'image', 'slug', 'author', 'category', 'content',
            'created_at', 'updated_at', 'status'
            )
        read_only_fields = ('author',)
