from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('a/', views.a, name='a'),
    path('b/', views.b, name='b'),
    path('c/', views.c, {'one': 'hello', 'two': 'world'}, name='c'),
    path('d/<int:pk>', views.d, name='d'),
]
