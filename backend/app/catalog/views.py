# coding: utf-8
import json
import django_filters
from django.views import View
from django.http import HttpResponse
from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ItemModel
from .serializer import ItemSerializer

from .domain.service.item import ItemService

#モデルをそのまま使わない場合はAPIViewかapi_viewを使う。
#ModelViewSetは使えない。
import requests
from rest_framework.views import APIView
from rest_framework.response import Response


# class ItemViewSet2(APIView):
#     def get(self, request):
#         # id = request.GET.get(key="id", default="1")
#         item_service = ItemService()
#         return Response(item_service.json(), status=200)

class ItemViewSet2(APIView):
    def get(self,request,*args, **kwargs):
        return Response({'some': 'data'})


# class ItemViewSet(viewsets.ViewSet):
#     # queryset = ItemModel.objects.all()
#     # print(ItemService.all())
#     item_service = ItemService()
#     print(item_service)
#     # queryset = item_service.all()
#     queryset = item_service
#     serializer_class = ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer