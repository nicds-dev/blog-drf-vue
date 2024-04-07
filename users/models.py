from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.exceptions import ValidationError

class CustomAccountManager(BaseUserManager):
    def create_user(self, email, user_name, first_name, last_name, password, **extra_fields):
        if not email:
            raise ValueError(
                'The Email must be provided'
                )

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must have is_staff=True.'
                )
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must have is_superuser=True.'
                )

        return self.create_user(email, user_name, first_name, last_name, password, **extra_fields)

class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(
        'about', max_length=500, blank=True, null=True
    )
    profile_image = models.ImageField(
        'profile image', upload_to='profile_image/', blank=True, null=True
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True) # Can be False for email verification

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name']

    def __str__(self):
        return self.user_name

class UserFollows(models.Model):
    user = models.ForeignKey(
        NewUser, on_delete=models.CASCADE, related_name='following'
    )
    followed_user = models.ForeignKey(
        NewUser, on_delete=models.CASCADE, related_name='followed_by'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'followed_user',)
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.user} follows {self.followed_user}'
    
    def clean(self):
        if self.user == self.followed_user:
            raise ValidationError('Users cannot follow themselves.')