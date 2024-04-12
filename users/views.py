from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer, UserSerializer, FollowerSerializer, FollowingSerializer, ResetPasswordSerializer
from .models import NewUser, UserFollows
from rest_framework_simplejwt.tokens import RefreshToken


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
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)