from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name',
            'birth_day', 'age', 'job_title', 'employer',
            'city', 'phone_number', 'profile_picture',
        ]