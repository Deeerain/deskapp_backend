from rest_framework import serializers

from applications.models import App
from comments.models import Comment

from api.users.serializers import UserSerializer


class CreateAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['theme', 'text']


class AppSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = App
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class AppWithCommentsSerializer(AppSerializer):
    comments = CommentSerializer(many=True)
