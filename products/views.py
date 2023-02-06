from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from .models import *
from .serializers import *


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
            return Response(serializer.error_messages, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
