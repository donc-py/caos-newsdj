from rest_framework import serializers
from .models import New, User
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')

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
        fields = ('nombre', 'noticia', 'email', 'documento', 'rut', 'telefono', 'ciudad')

    def create(self, validated_data):
        news = New.objects.create(
            nombre=validated_data['nombre'],
            noticia=validated_data['noticia'],
            email=validated_data['email'],
            documento=validated_data['documento'],
            rut=validated_data['rut'],
            telefono=validated_data['telefono'],
            ciudad=validated_data['ciudad'],
        )
        return news