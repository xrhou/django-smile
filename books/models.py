#!/usr/bin/python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models


# Create your models here.
# 出版社
class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=70)
    state_province = models.CharField(max_length=80)
    country = models.CharField(max_length=50)
    website = models.URLField()


# 书作者
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()


# 书
class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
