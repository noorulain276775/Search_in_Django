from django.urls import path
from .views import *
from rest_framework_swagger.views import get_swagger_view

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

schema_view = get_swagger_view(title='Django APIs')
urlpatterns = [
    #Swagger url for api documentation
    path('api_doc', schema_view),

    # JWT Authentication and User Registration
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register', RegisterUser.as_view()),
    path('refresh-token', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-verify', TokenVerifyView.as_view(), name='token_verify'),

    # JWT secured view of Products
    path('products', ProductsApiView.as_view()),
    path('products/create', ProductCreation.as_view()),
    path('products/<int:id>', ProductApiView.as_view()),

    # URLS of CART Item
    path('cartitems/create', CartItemsCreation.as_view()),
    path('cartitems', CartItemView.as_view()),
    path('cartitems/<int:id>', CartItemApiView.as_view()),

        # URLS of CART Item
    path('cart/create', CartCreation.as_view()),
    path('cart', CartView.as_view()),
    path('cart/<int:id>', CartDetailView.as_view()),

]
