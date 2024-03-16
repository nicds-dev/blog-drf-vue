from .views import PostList, PostDetail, PostListDetailFilter, ListPost, CreatePost, DetailPost, UpdatePost, DeletePost
from django.urls import path

app_name = 'blog_api'

urlpatterns = [
    path('', PostList.as_view(), name='listpost'),
    path('post/<str:pk>', PostDetail.as_view(), name='detailpost'),
    path('search/', PostListDetailFilter.as_view(), name='searchpost'),
    # Post Admin URLs
    path('admin/list', ListPost.as_view(), name='adminlistpost'),
    path('admin/create', CreatePost.as_view(), name='createpost'),
    path('admin/update/detail/<int:pk>', DetailPost.as_view(), name='admindetailpost'),
    path('admin/update/<int:pk>', UpdatePost.as_view(), name='updatepost'),
    path('admin/delete/<int:pk>', DeletePost.as_view(), name='deletepost'),
]

