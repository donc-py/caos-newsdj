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
        fields = ('title', 'descripcion')

    def create(self, validated_data):
        news = New.objects.create(
            title=validated_data['title'],
            descripcion=validated_data['descripcion'],
        )
        return news