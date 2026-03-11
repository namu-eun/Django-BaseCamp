from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def a(request):
    return HttpResponse('A 페이지입니다.')


def b(request):
    return HttpResponse('B 페이지입니다.')


def c(request, **kwargs):
    return HttpResponse(f'C 페이지입니다.{kwargs["two"]}')


def d(request, pk):
    return HttpResponse(f'D 페이지입니다. pk: {pk}')
