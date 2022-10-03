from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Article, models

def index(request):
    objs = Article.objects.all()
    context = {
        'articles': objs,
    }
    return render(request, 'blog/blogs.html', context)

def article(request, pk):
    obj = Article.objects.get(pk=pk)
    context = {
        'article': obj
    }
    return render(request, 'blog/article.html', context)