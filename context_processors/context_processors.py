from blog.models import Article, Category, Tag


def recentArticles(request):
    recent_articles = Article.objects.order_by('-created')[:3]

    return {'recent_articles': recent_articles}


def category(request):
    categories = Category.objects.all()[:5]

    return {'categories': categories}


def tag(request):
    tags = Tag.objects.all()[:5]

    return {'tags': tags}
