# main > view.py
from django.shortcuts import render
from django.http import HttpResponse

blog_list_db = [
    {
        "id": 1,
        "title": "장고는 너무 재미있어!!!",
        "content": "This is the content of blog 1",
        "author": "Author 1",
    },
    {
        "id": 2,
        "title": "파이썬도 너무 재미있어!!!!",
        "content": "This is the content of blog 2",
        "author": "Author 2",
    },
    {
        "id": 3,
        "title": "Life is too short, You need python!",
        "content": "This is the content of blog 3",
        "author": "Author 3",
    },
]

user_list_db = [
    {
        "id": 1,
        "username": "hojun",
        "email": "hojun@gmail.com",
        "password": "1234",
    },
    {
        "id": 2,
        "username": "jihun",
        "email": "jihun@gmail.com",
        "password": "1234",
    },
    {
        "id": 3,
        "username": "junho",
        "email": "junho@gmail.com",
        "password": "1234",
    },
]


def index(request):
    return HttpResponse("index")


def blog_list(request):
    context = {"blog_list": blog_list_db, "hello": [10, 20, 30]}
    return render(request, "main/blog_list.html", context)


def blog_details(request, pk):
    blog = blog_list_db[pk - 1]
    context = {"blog": blog}
    return render(request, "main/blog_details.html", context)


def accounts_details(request, username):
    finduser = None
    for user in user_list_db:
        if user["username"] == username:
            finduser = user
            break
    if finduser is None:
        return HttpResponse("User not found")
    context = {"user": finduser}
    return render(request, "main/accounts_details.html", context)