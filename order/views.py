from django.shortcuts import get_object_or_404
from rest_framework import generics,status
from rest_framework.response import Response
from . import serializers
from . models import Order
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from django.contrib.auth import get_user_model

User = get_user_model()

# Crud order start
class OrderCreateListView(generics.GenericAPIView):
    serializer_class = serializers.OrderCreationSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self,request):
        orders =Order.objects.all() 
        serializer = self.serializer_class(instance=orders,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        user = request.user

        if serializer.is_valid():
            serializer.save(customer = user)

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailView(generics.GenericAPIView):
    serializer_class = serializers.OrderDetailSerializer
    permission_classes = [IsAdminUser]
    def get(self,request,order_id):
        order = get_object_or_404(Order,pk=order_id)
        serializer = self.serializer_class(instance=order)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def put(self,request,order_id):
        data = request.data
        order = get_object_or_404(Order,pk=order_id)
        serializer = self.serializer_class(instance=order,data=data)

        if serializer.is_valid():
            serializer.save(customer=request.user)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class UpdateOrderStatusView(generics.GenericAPIView):
    serializer_class=serializers.OrderStatusUpdateSerializer
    permission_classes = [IsAdminUser]

    def put(self,request,order_id):
        order = get_object_or_404(Order, pk=order_id)
        data = request.data
        serializer = self.serializer_class(data=data,instance=order)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK) 

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserOrderView(generics.GenericAPIView):
    serializer_class = serializers.OrderDetailSerializer
    
    def get(self,request,user_id):
        print("User ID:", user_id) 
        user =User.objects.get(pk=user_id)
        order = Order.objects.all().filter(customer=user)
        serializer = self.serializer_class(instance=order,many=True)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK) 

class UserOrderDetailView(generics.GenericAPIView):
    serializer_class = serializers.OrderDetailSerializer

    def get(self,request,user_id,order_id):
        user = User.objects.get(pk=user_id)
        order = Order.objects.all().filter(customer=user).get(pk=order_id)
        serializer = self.serializer_class(instance=order)

        return Response(data=serializer.data,status=status.HTTP_200_OK)
# Crud order end