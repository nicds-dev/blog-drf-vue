from django.urls import path
from .views import (
    CustomUserCreate, UpdateUserView, ResetPasswordView, BlacklistTokenUpdateView,
    SingleUserView,FollowersListView, FollowingListView, FollowUserView, UnfollowUserView
    )

app_name = 'users'

urlpatterns = [
    path('account/register/', CustomUserCreate.as_view(), name='create_user'),
    path("account/edit/", UpdateUserView.as_view(), name="update_user"),
    path('account/reset-password/', ResetPasswordView.as_view(), name='reset_password'),
    path('account/logout/blacklist/', BlacklistTokenUpdateView.as_view(), name='blacklist'),
    path("<str:user_name>/", SingleUserView.as_view(), name="detail_user"),
    path("<str:user_name>/followers/", FollowersListView.as_view(), name="followers"),
    path("<str:user_name>/following/", FollowingListView.as_view(), name="following"),
    path("<str:user_name>/follow/", FollowUserView.as_view(), name="follow_user"),
    path("<str:user_name>/unfollow/", UnfollowUserView.as_view(), name="unfollow_user"),
]
