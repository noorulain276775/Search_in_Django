from rest_framework import generics
from rest_framework.response import Response
from rest_framework import filters
from django_filters import FilterSet, RangeFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.exceptions import APIException
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *


""""
------------------------------ PRODUCT FILTER AND SEARCH FUNCTIONALITY IMPLEMENTED ---------------------------------
"""
# Dynamic Search Filter
class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


## Range Filters for Price and Quantity
class ProductPriceQuantityFilter(FilterSet):
    price = RangeFilter()
    quantity = RangeFilter()

    class Meta:
        model = Products
        fields = ['price', 'quantity']

""""
------------------------------ REGISTRATION ---------------------------------------
"""

# User Registration View
class RegisterUser(generics.GenericAPIView):
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        except:
            raise APIException('Something went wrong')


""""
------------------------------ REST API VIEWS FOR PRODUCTS ---------------------------------------
------------------------------ SEARCH FUNCTIONALITY FOR PRODUCTS ---------------------------------------
"""

# Product API Views for GET-all products with search functionality
class ProductsApiView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    filter_backends = (DynamicSearchFilter, DjangoFilterBackend, filters.OrderingFilter )
    filterset_class = ProductPriceQuantityFilter
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    search_fields = ['category', 'brand', 'price', 'name',
                     'quantity', 'created_at', 'rating']
    ordering_fields = ['price', 'quantity', 'rating']


# Product API Views for Creating product
class ProductCreation(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    def perform_create(self, serializer):
        return serializer.save()


# Product API VIEW for GET-ONE product with update and delete
class ProductApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductsSerializer
    lookup_field= "id"

    def get_queryset(self):
        return Products.objects.filter()

    def update(self, request, id):
        queryset = Products.objects.filter(id=id).first()
        serializer = ProductsSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


""""
------------------------------ FOR CART ---------------------------------------
"""
# cartItem API Views for GET-all the CARTITEMS
class CartItemsApiView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


# cartItem API Views for putting a product Item in the cart
class CartItemCreation(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    def perform_create(self, serializer):
        return serializer.save()


# cartItem API VIEW for GET-ONE cartItem with update and delete
class CartItemApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()
    lookup_field= "id"

    def get_queryset(self):
        return CartItem.objects.filter()

    def update(self, request, id):
        queryset = CartItem.objects.filter(id=id).first()
        serializer = CartItemSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

""""
------------------------------ FOR CART ITEMS ---------------------------------------
"""
# cartItem API Views for GET-all the CARTITEMS
class CartItemsApiView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


# cartItem API Views for putting a product Item in the cart
class CartItemCreation(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    def perform_create(self, serializer):
        return serializer.save()


# cartItem API VIEW for GET-ONE cartItem with update and delete
class CartItemApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()
    lookup_field= "id"

    def get_queryset(self):
        return CartItem.objects.filter()

    def update(self, request, id):
        queryset = CartItem.objects.filter(id=id).first()
        serializer = CartItemSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)