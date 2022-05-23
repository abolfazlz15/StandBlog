from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Comment
from django.core.paginator import Paginator
from django.contrib.auth.models import User


def articleDetail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        Comment.objects.create(body=body, article=article, user=request.user, parent_id=parent_id)
        
    return render(request, 'blog/details.html', context={'article': article})


def blogList(request):
    articles = Article.objects.filter(published=True)

    paginator = Paginator(articles, 4)
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)

    return render(request, 'blog/blog.html', context={'articles': articles})


def categoryDetail(request, pk):
    category = get_object_or_404(Category, id=pk)
    articles = category.articles.all()

    paginator = Paginator(articles, 4)
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)

    return render(request, 'blog/blog.html', context={'articles': articles})


def searchBlog(request):
    search_form = request.GET.get('search_form')
    articles = Article.objects.filter(title__icontains=search_form)
    paginator = Paginator(articles, 4)
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)
    return render(request, 'blog/blog.html', context={'articles': articles})
