from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from django.shortcuts import get_object_or_404


class HomeView(APIView):
    def get(self, request):
        return Response("Order processing system")


class OrderCreateView(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderItemCreateView(APIView):
    def post(self, request, id):
        order = get_object_or_404(Order, id=id)
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            order_item = serializer.save(order=order)
            order.total_price += order_item.price * order_item.quantity
            order.save()
            return Response(OrderItemSerializer(order_item).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderTotalView(APIView):
    def get(self, request, id):
        order = get_object_or_404(Order, id=id)
        return Response({'order_id': order.id, 'total_price': order.total_price}, status=status.HTTP_200_OK)

