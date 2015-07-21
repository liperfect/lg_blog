from django.contrib import admin
from blog.blogapp.models import *
# Register your models here.
class Blog_listAdmin(admin.ModelAdmin):
    list_display =('title','timestamp')

admin.site.register(Blog_list,Blog_listAdmin,)

