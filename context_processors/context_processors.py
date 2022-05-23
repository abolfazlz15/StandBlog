from blog.models import Article, Category


def recentArticles(request):
    recent_articles = Article.objects.order_by('-created')[:3]

    return {'recent_articles': recent_articles}


def category(request):
    categories = Category.objects.all()[:5]

    return {'categories': categories}
