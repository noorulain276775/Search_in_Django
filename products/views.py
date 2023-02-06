from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.exceptions import APIException
from .models import *
from .serializers import *

# User Registration View
class RegisterUser(APIView):
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


# Product API Views for GET-all or POST
class ProductsApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            products = Products.objects.all()
            serializer = ProductsSerializer(products, many=True)
            return Response(serializer.data)
        except:
            raise APIException('Something went wrong')

    def post(self, request):
        try:
            serializer = ProductsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        except:
            raise APIException('Please Try Again')



# Product API VIEW for GET-ONE product with update and delete
class ProductApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            product = Products.objects.get(id=id)
            serializer = ProductsSerializer(product)
            return Response(serializer.data)
        except:
            raise APIException('Product Not Found')

    def put(self, request, id):
        try:
            product = Products.objects.filter(id=id).first()
            serializer = ProductsSerializer(
                product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        except:
            raise APIException('Product Not Found')

    def delete(self, request, id):
        try:
            product = Products.objects.filter(id=id).delete()
            return Response({'message': "the product has been deleted successfully"}, status=status.HTTP_202_ACCEPTED)
        except:
            raise APIException('Product not found')
