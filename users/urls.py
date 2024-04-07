from django.urls import path
from .views import CustomUserCreate, UpdateUserView, ResetPasswordView, BlacklistTokenUpdateView

app_name = 'users'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name='create_user'),
    path("update-user", UpdateUserView.as_view(), name="update_user"),
    path('reset-password', ResetPasswordView.as_view(), name='reset_password'),
    path('logout/blacklist', BlacklistTokenUpdateView.as_view(), name='blacklist'),
]