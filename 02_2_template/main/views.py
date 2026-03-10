from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')
    # main/index.html 이렇게 경로로 써줘야 settings.py에 설정한 템블릿을 순서대로 읽지 않고 해당 파일을 읽어올 수 있음

def about(request):
    return render(request, "main/about.html")

def contact(request):
    return render(request, "main/contact.html")
