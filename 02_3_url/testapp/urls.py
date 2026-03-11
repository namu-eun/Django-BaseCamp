from django.http import HttpResponse
from django.urls import path

urlpatterns = [
    path('', lambda request: HttpResponse('TestApp 입니다.')),
]
