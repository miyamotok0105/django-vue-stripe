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
from .domain.service.image import ImageService

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

class UploadImage(APIView):
    def get(self, request):
        image_service = ImageService()
        images = image_service.get_all()
        return JsonResponse(images, status=200, safe=False)

    # def post(self, request):
    #     id = request.POST.get("id", default="")
    #     image = request.POST.get("image", default="")

    #     image_service = ImageService()
    #     hoge = image_service.upload()
    #     return JsonResponse(hoge, status=200, safe=False)

class ChargeItem(APIView):
    def post(self, request):
        token = request.POST.get("token", default="")
        item = request.POST.get("item", default="")

        item_service = ItemService()
        charge = item_service.charge()
        return JsonResponse(charge, status=200, safe=False)


from .serializer import FileSerializer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .domain.service.file import FileService

class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def get(self, request):
        file_service = FileService()
        files = file_service.get_all()
        return JsonResponse(files, status=200, safe=False)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


