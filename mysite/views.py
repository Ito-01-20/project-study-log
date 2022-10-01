from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'Really site',
    }
    return render(request, 'mysite/index.html', context)