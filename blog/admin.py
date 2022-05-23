from django.contrib import admin
from .models import Category, Article, Comment

admin.site.register(Comment)


admin.site.register(Category)

# To personalize the admin panel
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # for show customization list objects
    list_display = ('title', 'slug', 'author', 'published')
    list_filter = ('published', 'author', 'created')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    # date_hierarchy = 'created'
    ordering = ('status',)
    list_editable = ('published',)
    list_display_links = ('title', 'slug',)
