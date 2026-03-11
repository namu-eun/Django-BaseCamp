from django.db.models import Q
from django.shortcuts import render, redirect

from .models import Post


def blog_list(request):
    if request.GET.get("q"):
        q = request.GET.get("q")
        blogs = Post.objects.filter(
            Q(title__icontains=q) & Q(content__icontains=q)
        ).distinct()
    else:
        blogs = Post.objects.all()
    context = {"object_list": blogs}
    return render(request, "blog/blog_list.html", context)


def blog_detail(request, pk):
    blog = Post.objects.get(pk=pk)
    context = {'object': blog}
    return render(request, 'blog/blog_detail.html', context)


def blog_create(request, title):
    contents = f"hello world {title}"
    Post.objects.create(title=title, content=contents)
    return redirect('blog_list')


def blog_delete(request, pk):
    q = Post.objects.get(pk=pk)
    q.delete()
    return redirect("blog_list")
