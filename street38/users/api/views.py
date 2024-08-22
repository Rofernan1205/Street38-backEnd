from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from users.models import User
from users.api.serializers import UserSerializer

class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    
    