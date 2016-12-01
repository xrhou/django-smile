#!/usr/bin/python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
# 出版社
@python_2_unicode_compatible
class Publisher(models.Model):
    name = models.CharField(max_length=50, verbose_name='出版社名称')
    address = models.CharField(max_length=50, verbose_name='详细地址')
    city = models.CharField(max_length=70, verbose_name='市')
    state_province = models.CharField(max_length=80, verbose_name='省')
    country = models.CharField(max_length=50, verbose_name='所属国家')
    website = models.URLField(verbose_name='网站')

    def __str__(self):
        return self.name

    # 默认排序方式
    class Meta:
        ordering = ['name']


# 书作者
@python_2_unicode_compatible
class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='FirstName')
    last_name = models.CharField(max_length=40, verbose_name='LastName')
    mobile = models.CharField(max_length=20, verbose_name='联系电话')
    email = models.EmailField(blank=False, verbose_name='邮箱')

    def __str__(self):
        return u'%s%s' % (self.first_name, self.last_name)


# 书
@python_2_unicode_compatible
class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='书名')
    authors = models.ManyToManyField(Author, verbose_name='作者')
    publisher = models.ForeignKey(Publisher, verbose_name='出版社')
    publication_date = models.DateField(blank=True, verbose_name='出版日期')

    def __str__(self):
        return self.title
