# coding: utf-8
from django.urls import path, include
from rest_framework import routers

from .views import ItemViewSet
from .views import ItemViewSet2
from . import views

router = routers.DefaultRouter()
# router = routers.SimpleRouter()

router.register(r'items', ItemViewSet)
router.register(r'items2', ItemViewSet)

# urlpatterns = [
#     path('',include(router.urls)),
#     path('articals/',views.ArticalView.as_view()),
#     path('<int:pk>/',views.ArticalView.as_view()),
#     path('auth/login',views.LogInView.as_view()),
#     path('auth/logout',views.LogOutView.as_view()),
#     path('register/',views.Register.as_view()),
# ]
#https://github.com/kishorkumarsaini/ArticalRestAPI/blob/master/api_view/artical/urls.py
