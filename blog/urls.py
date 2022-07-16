from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('detail/<slug:slug>', views.articleDetail, name='details'),
    path('', views.blogList, name='blog'),
    path('category/<int:pk>', views.categoryDetail, name='category_detail'),
    path('search/', views.searchBlog, name='search'),
    path('like/<slug:slug>/<int:id>', views.likeArticle, name='like'),
]
