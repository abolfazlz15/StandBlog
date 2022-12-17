from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .models import Article, Category, Comment, Like, Tag


def articleDetail(request, slug):
    article = get_object_or_404(Article, slug=slug)

    number_of_comments  = article.comments.count() 
    number_of_like  = article.likes.count() 
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        Comment.objects.create(body=body, article=article, user=request.user, parent_id=parent_id)  

    # like system
    if request.user.likes.filter(article__slug=slug, user_id=request.user.id).exists(): # if user like article show in templets
        is_liked = True
    else:
        is_liked = False    

    context={
        'article': article,
        'number_of_comments': number_of_comments,
        'is_liked': is_liked,
        'number_of_like': number_of_like,
        }
    return render(request, 'blog/details.html', context)


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


def tagDetail(request, pk):
    tag = get_object_or_404(Tag, id=pk)
    articles = tag.articles.all()

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


def likeArticle(request, slug, id):
    try:
        like = Like.objects.get(article__slug=slug, user_id=request.user.id)
        like.delete()
    except:
        Like.objects.create(article_id=id, user_id=request.user.id)

    return redirect('blog:details', slug)
