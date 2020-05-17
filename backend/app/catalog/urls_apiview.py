# coding: utf-8

from django.urls import path, include
from django.conf.urls import url

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='API Lists')

from .views import ItemViewSet
from .views import ItemViewSet2, ChargeItem
from .views import UploadImage
from .views import FileView

urlpatterns = [
    path('items4/', ItemViewSet2.as_view()),
    path('charge/', ChargeItem.as_view()),
    path('image/', UploadImage.as_view()),
    url(r'upload/', FileView.as_view(), name='file-upload'),
    url(r'^swagger/', schema_view),
]



