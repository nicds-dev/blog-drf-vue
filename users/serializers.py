from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import NewUser, UserFollows
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


def _validate_password(password):
    if len(set(password.lower())) <= 4:
        raise ValidationError('Password must contain at least 5 unique characters')


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_name'] = user.user_name
        return token

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password, _validate_password])
    class Meta:
        model = NewUser
        fields = ('id', 'email', 'user_name', 'first_name', 'last_name', 'about', 'profile_image', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    num_posts = serializers.SerializerMethodField()
    num_followers = serializers.SerializerMethodField()
    num_following = serializers.SerializerMethodField()

    def get_num_posts(self, obj):
        return obj.blog_posts.count()

    def get_num_followers(self, obj):
        return obj.followers.count()

    def get_num_following(self, obj):
        return obj.following.count()

    class Meta:
        model = NewUser
        fields = (
            'id', 'email', 'user_name', 'first_name', 'last_name', 'profile_image', 'about',
            'start_date', 'num_posts', 'num_followers', 'num_following'
        )
        read_only_fields = ('email', 'start_date',)

class FollowerSerializer(serializers.ModelSerializer):
    follower = serializers.CharField(source='follower.user_name')
    class Meta:
        model = UserFollows
        fields = ('id', 'follower', 'created_at')

class FollowingSerializer(serializers.ModelSerializer):
    following = serializers.CharField(source='following.user_name')
    class Meta:
        model = UserFollows
        fields = ('id', 'following', 'created_at')

class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise ValidationError('The two password fields didn`t match.')
        try:
            validate_password(data['new_password'])
            _validate_password(data['new_password'])
        except ValidationError as err:
            raise ValidationError({'password': err})
        return data