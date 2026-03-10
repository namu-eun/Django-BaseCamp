# config > urls.py

from django.contrib import admin
from django.urls import path, include
from main.view import index, blog_list, blog_details, accounts_details
#view.py에 정의할 함수들을 사용할 수 있게 불러옵니다.

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index),
    path('blog/', blog_list),
    path('blog/<int:pk>/', blog_details),
    path('accounts/<str:username>/', accounts_details),
]
