from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'username' ,'name']

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email

        return name

