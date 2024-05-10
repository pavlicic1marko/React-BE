from rest_framework import serializers
from django.contrib.auth.models import User
from  rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = User
        fields = ['id', 'email', 'username' ,'name' , '_id', 'isAdmin']

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email

        return name

    def get__id(self, obj):
        _id = obj.id
        return _id

    def get_isAdmin(self, obj):
        return obj.is_staff



class UserSerializerWithToken(UserSerializer): #Used after updating user information
    token = serializers.SerializerMethodField(read_only=True)
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'username' ,'name' , '_id', 'isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return  str(token.access_token)

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email

        return name

    def get__id(self, obj):
        _id = obj.id
        return _id

    def get_isAdmin(self, obj):
        return obj.is_staff
