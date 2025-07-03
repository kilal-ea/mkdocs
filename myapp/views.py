from django.shortcuts import render
from .models import Article

def home(request):
    articles = Article.objects.all()
    return render(request, 'home.html', {'articles': articles})



from django.shortcuts import redirect

def docs_func_redirect(request):
    return redirect('/static/docs_site/Documentation_Fonctionnelle/index.html')