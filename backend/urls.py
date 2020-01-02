# coding: utf-8

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from backend.app.catalog.urls import router as catalog_router
from backend.app.catalog import urls_apiview
from backend.app.catalog import views



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(catalog_router.urls)),
    #includeでサブアプリのurlをインクルードする
    #https://qiita.com/himrock922/items/bd020a0d313233556c97
    url(r'^api/', include(urls_apiview)),

    path('api/items3/', views.ItemViewSet2.as_view()),
]
