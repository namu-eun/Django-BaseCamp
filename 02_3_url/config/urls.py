from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('test/', include('testapp.urls')),
    re_path(r"re/(?P<value>[0-9]{4})/", lambda request, value: HttpResponse(f're_path {value}입니다.')),
]
