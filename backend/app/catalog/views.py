# coding: utf-8
import json
from decimal import Decimal
import django_filters
from django.views import View
from django.http import HttpResponse, JsonResponse
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


class ItemViewSet(viewsets.ModelViewSet):
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer



class ItemViewSet2(APIView):
    def get(self, request):
        # id = request.GET.get(key="id", default="1")
        item_service = ItemService()
        items = item_service.all()
        return JsonResponse(items, status=200, safe=False)
        