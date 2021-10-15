from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False, write_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "birth_day",
            "age",
            "job_title",
            "employer",
            "city",
            "phone_number",
            "profile_picture",
            "is_staff",
            "password",
        ]


class UserSerializationWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    password = serializers.CharField(required=False, write_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "birth_day",
            "age",
            "job_title",
            "employer",
            "city",
            "phone_number",
            "profile_picture",
            "password",
            "is_staff",
            "token",
        ]

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token
