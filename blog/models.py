from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import format_html



class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    publish = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='articles')
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='image/article')
    time_publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    published = models.BooleanField(default=True)

    
    class Meta: # --change from root--
        ordering = ('-created',)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('blog:details', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.title} - {self.body[:30]}'

    def showImage(self):
        # show image in admin panel
        if self.image:
            return format_html(f'<img src="{self.image.url}" alt="" width="50px" height="50px">')
        else:
            return format_html(f'<h4>مقاله {self.title} تصویر ندارد</h4>')
    showImage.short_description = 'تصویر'



class Tag(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    publish = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user} - {self.body[:40]}'
