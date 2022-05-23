from django.shortcuts import render
from blog.models import *


def home(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    # recent_articles = Article.objects.all().order_by('-updated')

    context = {
        'articles': articles,
        'categories': categories,
        # 'recent_articles': recent_articles,
    }

    return render(request, 'home/index.html', context)
