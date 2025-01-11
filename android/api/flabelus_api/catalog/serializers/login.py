from rest_framework import serializers
from ..models import User, Store

class UserLoginSerializer(serializers.ModelSerializer):
    """
    Serializer for user information during login.
    """
    role = serializers.CharField(source='role.name')  # Role name

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'profile_picture', 'role']


class StoreSerializer(serializers.ModelSerializer):
    """
    Serializer for store information during login.
    """
    class Meta:
        model = Store
        fields = ['id', 'name', 'location']