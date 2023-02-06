from django.urls import path
from .views import RegisterUser, ProductsApiView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [

    ## JWT Authentication and User Registration
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register', RegisterUser.as_view()),
    path('refresh-token', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-verify', TokenVerifyView.as_view(), name='token_verify'),
    

    ## JWT secured view of Products
    path('products', ProductsApiView.as_view()),
]