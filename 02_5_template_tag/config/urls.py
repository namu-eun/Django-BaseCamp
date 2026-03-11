# urls.py
from datetime import datetime

from django.shortcuts import render
from django.urls import path


def example_view(request):
    context = {
        'user': {
            'name': '홍길동',
            'email': 'hong@example.com',
            'age': 25,
        },
        'posts': [
            {'title': '첫 번째 글',
             'content': '안녕하세요.\n첫 번째 글입니다.',
             'date': datetime(2023, 7, 1)},
            {'title': '두 번째 글',
             'content': '반갑습니다.\n두 번째 글입니다.',
             'date': datetime(2023, 7, 15)},
            {'title': '세 번째 글',
             'content': '안녕히 가세요.\n세 번째 글입니다.',
             'date': datetime(2023, 7, 30)},
        ],
        'numbers': list(range(1, 11)),
    }
    return render(request, 'example.html', context)


urlpatterns = [
    path('example/', example_view),
]
