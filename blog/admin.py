from django.contrib import admin
from .models import Category, Article, Comment
from django.contrib import messages
from django.utils.translation import ngettext

# header admin panel
admin.site.site_header = 'SandBlog Admin Panel'

admin.site.register(Comment)
admin.site.register(Category)

class CommentInLine(admin.StackedInline): # for show comment in article detail (Django admin panel)
    model = Comment


# To personalize the admin panel
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # for show customization list objects
    fields = ('title', 'author', 'category', 'body', 'image', 'status', 'published', 'time_publish', 'slug')
    list_display = ('showImage', 'title', 'slug', 'author', 'published')
    list_filter = ('published', 'author', 'created')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    ordering = ('status',)
    list_editable = ('published',)
    list_display_links = ('title', 'slug',)
    inlines = (CommentInLine,)
    actions = ['make_published']

    @admin.action(description='Mark selected articles as published')
    def make_published(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, ngettext(
            '%d story was successfully marked as published.',
            '%d stories were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Mark selected articles as hide')
    def make_published(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, ngettext(
            '%d story was successfully marked as hide.',
            '%d stories were successfully marked as hide.',
            updated,
        ) % updated, messages.SUCCESS)
