# coding: utf-8
import json
from decimal import Decimal
import django_filters
from django.views import View
from rest_framework import viewsets, filters
from rest_framework.response import Response

from .models import ItemModel
from .serializer import ItemSerializer
from .domain.service.item import ItemService

class ItemViewSet(viewsets.ModelViewSet):
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer

#モデルをそのまま使わない場合はAPIViewかapi_viewを使う。
#ModelViewSetは使えない。
import requests
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse

class ItemViewSet2(APIView):
    def get(self, request):
        # id = request.GET.get(key="id", default="1")
        item_service = ItemService()
        items = item_service.get_all()
        return JsonResponse(items, status=200, safe=False)

class ChargeItem(APIView):
    def post(self, request):
        token = request.POST.get("token", default="")
        item = request.POST.get("item", default="")

        item_service = ItemService()
        charge = item_service.charge()
        return JsonResponse(charge, status=200, safe=False)
