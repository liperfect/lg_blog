from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from blog.blogapp.models import *


def index(request):
    posts = Blog_list.objects.all()
    return render_to_response('index.html',locals())



def success(request):
    return render_to_response('success.html',locals())

def blog(request):
   return render_to_response('blog.html',locals())
