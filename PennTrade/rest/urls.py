from django.urls import path
from .views import *

urlpatterns = [
    path('product/', ProductList.as_view(), name="product_list"),
    path('product/<int:pk>', ProductDetail.as_view(), name="product_detail"),
    path('user/', UserCreate.as_view(), name="user_create"),
    path('user/products/', UserProducts.as_view(), name="user_products"),
    path('user/detail/<username>', UserDetail.as_view(), name = "user_detail"),
    path('user/message/', Messages.as_view(), name="send_message"),
    path('login/', Login.as_view(), name="login_view"),
]
