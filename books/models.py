#!/usr/bin/python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
# 出版社
@python_2_unicode_compatible
class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=70)
    state_province = models.CharField(max_length=80)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

    #默认排序方式
    class Meta:
        ordering = ['name']


# 书作者
@python_2_unicode_compatible
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)


# 书
@python_2_unicode_compatible
class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
