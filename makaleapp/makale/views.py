from django.shortcuts import render, get_object_or_404
from .models import Category, Article,Bugün,afiş,daha_yenilik,daha_sorular


def index(request):
    data = {
        'categories': Category.objects.all(),
        'articles': Article.objects.all(),
        'afişler':afiş.objects.all(),
       
    }
    return render(request, 'makale/index.html',data)



def category_list(request):
    data = {
        'categories':  Category.objects.all(),
    }
    return render(request,'makale/category_list.html',data)


def bugün(request):
    data = {
        'categories':  Category.objects.all(),
        'Bugüns': Bugün.objects.all(),
    }
    return render(request,'makale/bugün.html',data)

       
def sözlük(request):
    return render(request,'makale/sözlük.html')

def daha(request):
    data = {
        'dahay':  daha_yenilik.objects.all(),
        'dahas':  daha_sorular.objects.all(),
    }
    return render(request,'makale/daha.html',data)

def bir_fikrim_var(request):
    return render(request,'makale/bir_fikrim_var.html')

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    articles = category.articles.all()
    return render(request, 'makale/category_detail.html', {'category': category, 'articles': articles})

def article_detail (request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'makale/article_detail.html', {'article': article})
               
