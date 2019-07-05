from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import ProductSerializer, UserSerializer
from .models import Product


# Create your views here.
class ProductList(generics.ListAPIView):
    permission_classes = ()
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductDetail(generics.RetrieveAPIView):
    permission_classes = ()
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Only the user who created a product can update/destroy that product


# Only the user who's account this is can update their own details

class UserProducts(generics.ListCreateAPIView):
    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)
    serializer_class = ProductSerializer

class UserCreate(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = User.objects.all()
    serializer_class = UserSerializer

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

class UserDetail(generics.RetrieveAPIView):
    permission_classes = ()
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'

## Simulate Buying a product
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
class SendMessage(APIView):
    def post(self, request):
        pass

