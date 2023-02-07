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


# Search Filter
class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


## Range Filters
class ProductPriceQuantityFilter(FilterSet):
    price = RangeFilter()
    quantity = RangeFilter()

    class Meta:
        model = Products
        fields = ['price', 'quantity']


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

