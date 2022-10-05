from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from blog.models import Article
from mysite.forms import UserCreationForm
from django.contrib import messages

def index(request):
    objs = Article.objects.all()
    context = {
        'title': 'Really site',
        'articles': objs,
    }
    return render(request, 'mysite/index.html', context)


class Login(LoginView):
    template_name = 'mysite/auth.html'
    
def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.sava(commit=False)
            # user.is_active = False
            user.save()
            messages.success(request, '登録完了!')
            return redirect('/')
    return render(request, 'mysite/auth.html', context)