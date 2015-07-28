from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from blog.apps.article.models import Article


def index(request):
    posts = Article.objects.all()
    return render_to_response('index.html',locals())


def success(request):
    return render_to_response('success.html',locals())


def blog(request):
   return render_to_response('blog.html',locals())
