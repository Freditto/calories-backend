from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'phone',
            # 'name',
            # 'type',
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        email = self.validated_data['email']
        password = self.validated_data['password']
        username = self.validated_data['username']
        phone = self.validated_data['phone']
        # name = self.validated_data['name']
        # type = self.validated_data['type']
        user = User.objects.create_user(username=username, password=password, email=email, phone=phone)
        return user

