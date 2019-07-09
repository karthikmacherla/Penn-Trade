from rest_framework import serializers
from .models import Product, Message
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Figure out OAuth / Third Party Authentication Scheme
# Add profile picture to model 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user = user)
        return user


class ProductSerializer(serializers.ModelSerializer):
    status = serializers.PrimaryKeyRelatedField(queryset=Product.STATUS_CHOICES)
    owner = UserSerializer()
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'owner')
        depth = 1


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'