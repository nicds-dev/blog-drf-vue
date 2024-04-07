from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import NewUser


class RegisterUserSerializer(serializers.ModelSerializer):
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
            self._validate_password(password)
            instance.set_password(password)
        instance.save()
        return instance

    def _validate_password(self, password):
        try:
            validate_password(password)
            if len(set(password.lower())) <= 4:
                raise ValidationError('Password must contain at least 5 unique characters')
        except ValidationError as err:
            raise ValidationError({'password': err.messages})

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('user_name', 'first_name', 'last_name', 'about', 'profile_image')

class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise ValidationError('Passwords do not match')
        return data