from django.contrib import admin
from blog.apps.article.models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display =('title', 'timestamp')

admin.site.register(Article, ArticleAdmin)
