from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import User
from .import serializers

# Create your views here.

class HelloAuthView(generics.GenericAPIView):
    @swagger_auto_schema(operation_summary="Hello Auth")
    def get(self,request):
        return Response(data={"message": "hello Auth"},status=status.HTTP_200_OK)

#user creation api start   
class UserCrateView(generics.GenericAPIView):
    serializer_class = serializers.UserCreationSerializer
    
    @swagger_auto_schema(operation_summary="Create a User account")
    def post(self,request):
        data = request.data

        serializers= self.serializer_class(data=data)

        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        
        return Response(data=serializers.errors,status=status.HTTP_400_BAD_REQUEST)
#user creation api end