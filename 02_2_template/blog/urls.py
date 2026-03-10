from django.urls import path

from . import views

urlpatterns = [
    # blog/
    path('', views.blog_list, name='blog_list'),  # blog/로 연결
    # blog/1/
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
]
