from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import decorators

from api.deskapp import serializers
from api.deskapp import permissions as custom_permissions

from applications.models import App


class AppViewset(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = serializers.AppWithCommentsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateAppSerializer

        if (self.action == 'list'):
            return serializers.AppWithCommentsSerializer

        return super().get_serializer_class()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    @decorators.permission_classes([custom_permissions.IsOwnerOrAdmin])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @decorators.permission_classes([custom_permissions.IsOwnerOrAdmin])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @decorators.permission_classes([custom_permissions.IsOwnerOrAdmin])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
