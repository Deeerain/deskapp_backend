from rest_framework import serializers

from users.models import User, Position, Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class PositionSerialiser(serializers.ModelSerializer):
    departament = DepartmentSerializer()

    class Meta:
        model = Position
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    position = PositionSerialiser()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'position', 'last_login', 'is_staff']
