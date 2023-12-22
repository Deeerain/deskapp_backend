from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from users.models import User, Position, Department

from api.users import serializers


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['GET'], detail=False)
    def me(self, request: Request) -> Response:
        user = self.get_queryset().filter(
            username=request.user.username).first()
        serialiser = self.get_serializer(user)
        return Response(serialiser.data, status.HTTP_200_OK)


class PositionViewset(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = serializers.PositionSerialiser
    permission_classes = [permissions.IsAdminUser]


class DepartmentViewset(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    permission_classes = [permissions.IsAdminUser]
