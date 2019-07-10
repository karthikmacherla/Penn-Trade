from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import ProductSerializer, UserSerializer, MessageSerializer
from .models import Product, Message


# Allows anyone to see the available list of products
class ProductList(generics.ListAPIView):
    permission_classes = ()
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Allows anyone to get the data pertaining to one
# product
class ProductDetail(generics.RetrieveAPIView):
    permission_classes = ()
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Allows user to create a product in their name
class UserProducts(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Allows for creation of a new user/listing users
class UserCreate(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Allow you to login 
class Login(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong credentials"}, status=status.HTTP_400_BAD_REQUEST)

# Allows anyone to get details on a user
class UserDetail(generics.RetrieveAPIView):
    permission_classes = ()
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'

# Allows user to 'buy' a product from another user
class BuyProduct(APIView):
    def post(self, request):
        product = Product.objects.get(pk=request.data.get('pk'))
        if product.status != 'AVAILABLE':
            return Response({"message": "Sorry, cannot buy an unavailable product."}, 
            status=status.HTTP_400_BAD_REQUEST)
        # show that you can make the purchase somehow
        product.status = 'SOLD'
        # Send message to owner somehow
        # INCOMPLETE

# Allows user to send message to another user
class Messages(generics.ListCreateAPIView):
    permission_classes = ()
    queryset = Message.objects.all()
    serializer_class = MessageSerializer