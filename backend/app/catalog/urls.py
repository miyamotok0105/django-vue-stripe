# coding: utf-8

from rest_framework import routers
from .views import ItemViewSet

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)


