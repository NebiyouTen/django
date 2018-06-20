from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from companies.models import stock
from companies.serializer import StockSerializer


class StockList(APIView):

    def get(self,request):
        stocks = stock.objects.all()
        serial = StockSerializer(stocks,many=True)
        return Response(serial.data)

    def post(self):
        pass

