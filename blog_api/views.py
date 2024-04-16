from django.shortcuts import get_object_or_404
from blog.models import Post, Category, Comment
from .serializers import PostSerializer, CategorySerializer, CommentSerializer, LikeSerializer
from rest_framework import generics, permissions, status, filters
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

# User Permissions
class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'Editing posts is restricted to the author only.'
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


# Category View
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Display Post Views General
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveAPIView):
    serializer_class = PostSerializer

    def get_object(self):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)


# Search Post Views
class PostListDetailFilterView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['slug', 'category__id']


# Post Comment & Like Views
class CommentListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        data = {'post': post.pk, 'author': request.user.pk, **request.data}
        serializer = CommentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def delete(self, request, *args, **kwargs):
        try:
            comment = self.get_object()
        except Comment.DoesNotExist:
            return Response({'error': 'Comment not found'} ,status=status.HTTP_404_NOT_FOUND)
        
        if comment.author != request.user:
            return Response({'error': 'You are not authorized to delete this comment'}, status=status.HTTP_403_FORBIDDEN)
        
        comment.delete()
        return Response({'message': 'Comment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# Admin Post Views
class PostListAdminView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

class PostCreateAdminView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostUpdateAdminView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_object(self):
        queryset = Post.objects.filter(author=self.request.user)
        item = get_object_or_404(queryset, pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, item)
        return item

class PostDeleteAdminView(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
