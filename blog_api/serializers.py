from rest_framework import serializers
from blog.models import Post, Category, Comment, Like
from django.conf import settings

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.user_name', read_only=True)
    author_pic = serializers.CharField(source='author.profile_image', read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'author_name', 'author_pic', 'content', 'created_at', 'parent')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'post', 'author', 'created_at')

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.user_name', read_only=True)
    author_pic = serializers.CharField(source='author.profile_image', read_only=True)
    author_bio = serializers.CharField(source='author.about', read_only=True)
    category = CategorySerializer(read_only=True)
    num_comments = serializers.SerializerMethodField()
    def get_num_comments(self, obj):
        return obj.comments.count()
    class Meta:
        model = Post
        fields = (
            'id', 'title', 'image', 'slug', 'author', 'author_name', 'author_pic', 'author_bio', 'category', 'content', 'num_comments',
            'created_at', 'updated_at', 'status'
            )
        read_only_fields = ('author', )