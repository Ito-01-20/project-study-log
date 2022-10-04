from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article

def index(request):
    objs = Article.objects.all()
    context = {
        'title': 'Really site',
        'articles': objs,
    }
    return render(request, 'mysite/index.html', context)


def login(request):
    context = {}
    return render(request, 'mysite/login.html', context)