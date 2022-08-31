from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from django.contrib.auth.hashers import make_password

from auth_core.models import User
from auth_core.exceptions import InvalidPassword2Exception


class UserSerializer(ModelSerializer):
    email = serializers.EmailField(required=True, allow_blank=False, allow_null=False)
    username = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=50, min_length=8)
    password = serializers.CharField(
        required=True,
        allow_blank=False,
        allow_null=False,
        max_length=50,
        min_length=12,
        write_only=True,
    )
    password2 = serializers.CharField(
        required=True,
        allow_blank=False,
        allow_null=False,
        max_length=50,
        min_length=12,
        write_only=True,
    )

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'password',
            'password2',
            'created_time',
            'modified_time',
        )
        read_only_fields = ('id', 'username')

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        if validated_data['password'] != validated_data['password2']:
            raise InvalidPassword2Exception()
        else:
            validated_data.pop('password2')
        return validated_data

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)
