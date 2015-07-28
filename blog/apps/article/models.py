from django.contrib import admin
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    def __unicode__(self):
        return u'%s %s' % (self.title, self.timestamp)
