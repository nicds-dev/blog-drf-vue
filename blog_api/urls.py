from .views import (
    CategoryListView, PostListView, PostDetailView,
    CommentListCreateView, CommentDeleteView, LikeView,
    PostListAdminView, PostCreateAdminView, PostUpdateAdminView, PostDeleteAdminView
    )
from django.urls import path

app_name = 'blog_api'

urlpatterns = [
    path('', PostListView.as_view(), name='list-post'),
    path('categories/', CategoryListView.as_view(), name='list-category'),
    path('post/<str:pk>/', PostDetailView.as_view(), name='detail-post'),
    path('post/<slug:slug>/comments/', CommentListCreateView.as_view(), name='post-comments'),
    path('post/<slug:slug>/comment-delete/<int:pk>/', CommentDeleteView.as_view(), name='delete-comment'),
    path('post/<slug:slug>/likes/', LikeView.as_view(), name='post-likes'),
    # Post Admin URLs
    path('admin/list/', PostListAdminView.as_view(), name='adminlist-post'),
    path('admin/create/', PostCreateAdminView.as_view(), name='create-post'),
    path('admin/update/<int:pk>/', PostUpdateAdminView.as_view(), name='update-post'),
    path('admin/delete/<int:pk>/', PostDeleteAdminView.as_view(), name='delete-post'),
]

