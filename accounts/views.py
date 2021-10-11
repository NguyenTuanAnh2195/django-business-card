from django.http import Http404
from rest_framework import generics, permissions

from .models import User
from .serializers import UserSerializer
from .permissions import IsSelfOrAdminOrReadOnly


class UserList(generics.ListCreateAPIView):
    """
    List all users, or create a new user
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an User
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSelfOrAdminOrReadOnly]
    
