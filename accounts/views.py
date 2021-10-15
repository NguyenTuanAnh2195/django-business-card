from rest_framework import generics, permissions, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer, UserSerializationWithToken
from .permissions import IsSelfOrAdminOrReadOnly


@api_view(["GET"])
def current_user(request):
    """
    return current user by token
    """
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserCreate(generics.CreateAPIView):
    """
    Enable user to signup
    """

    queryset = User.objects.all()
    serializer_class = UserSerializationWithToken
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class UserList(generics.ListCreateAPIView):
    """
    List all users, or create a new user
    """

    queryset = User.objects.all()
    serializer_class = UserSerializationWithToken
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["age", "job_title", "employer", "city"]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update or Delete an User
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsSelfOrAdminOrReadOnly,
    ]
