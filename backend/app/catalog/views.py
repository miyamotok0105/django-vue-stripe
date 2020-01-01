# coding: utf-8
import django_filters
from rest_framework import viewsets, filters

from .models import Item
from .serializer import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

