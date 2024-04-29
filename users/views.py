from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (
    RegisterUserSerializer, CustomTokenObtainPairSerializer,
    UserSerializer,FollowerSerializer, FollowingSerializer, ResetPasswordSerializer
    )
from .models import NewUser, UserFollows
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomUserCreate(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        if request.user.is_authenticated:
            return Response({"error": "You are already logged in, please log out first"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class SingleUserView(generics.RetrieveAPIView):
    queryset = NewUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        username = self.kwargs.get('user_name')
        return generics.get_object_or_404(NewUser, user_name=username)

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)
        
class UpdateUserView(generics.RetrieveUpdateAPIView):
    queryset = NewUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
    
class ResetPasswordView(generics.UpdateAPIView):
    serializer_class = ResetPasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.object.set_password(serializer.validated_data.get('new_password'))
            self.object.save()

            return Response({'message': 'Password updated successfully.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# followers/following views
class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_name):
        try:
            user_to_modify = NewUser.objects.get(user_name=user_name)
        except NewUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        if user_to_modify == request.user:
            return Response({"error": "You cannot follow/unfollow yourself"}, status=status.HTTP_400_BAD_REQUEST)

        follow_instance, created = UserFollows.objects.get_or_create(
            follower=request.user, following=user_to_modify
        )
        if 'follow' in request.data:
            if created:
                return Response({"message": f"You are now following {user_name}"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": f"You are already following {user_name}"}, status=status.HTTP_400_BAD_REQUEST)
        elif 'unfollow' in request.data:
            if follow_instance:
                follow_instance.delete()
                return Response({"message": f"You have unfollowed {user_name}"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": f"You are not following {user_name}"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)

class FollowersListView(generics.ListAPIView):
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_name = self.kwargs['user_name']
        user = NewUser.objects.get(user_name=user_name)
        return UserFollows.objects.filter(following=user)

class FollowingListView(generics.ListAPIView):
    serializer_class = FollowingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_name = self.kwargs['user_name']
        user = NewUser.objects.get(user_name=user_name)
        return UserFollows.objects.filter(follower=user)


class BlacklistTokenUpdateView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'User logout successfully'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_400_BAD_REQUEST)