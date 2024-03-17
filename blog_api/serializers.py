from rest_framework import serializers
from blog.models import Post, Category
from django.conf import settings

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class PostSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Post
        fields = ('category', 'category_name', 'id', 'title', 'image', 'slug', 'author', 'excerpt', 'content', 'published', 'status')
        read_only_fields = ('author',)
