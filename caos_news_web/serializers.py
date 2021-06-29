from rest_framework import serializers
from .models import New, User
from django.contrib.auth import get_user_model
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')

class UserSerializer2(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email','username')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],email=validated_data['email'], password=validated_data['password'])

        return user

# Register News Serializer
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ('nombre', 'noticia', 'email', 'documento', 'pasaporte', 'telefono', 'ciudad')

    def create(self, validated_data):
        news = New.objects.create(
            nombre=validated_data['nombre'],
            noticia=validated_data['noticia'],
            email=validated_data['email'],
            documento=validated_data['documento'],
            pasaporte=validated_data['pasaporte'],
            telefono=validated_data['telefono'],
            ciudad=validated_data['ciudad'],
        )
        return news