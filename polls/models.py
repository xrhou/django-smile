#!/usr/bin/python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


# Create Question models here.
@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


# Create Choice models here.
@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# create 乐队
# class Band(models.Model):
#     """A model of a rock band."""
#     name = models.CharField(max_length=200)
#     can_rock = models.BooleanField(default=True)


# create 乐队成员
# class Member(models.Model):
#     """A model of a rock band member."""
#     name = models.CharField("Member's name", max_length=200)
#     instrument = models.CharField(choices=(
#         ('g', "Guitar"),
#         ('b', "Bass"),
#         ('d', "Drums"),
#     ),
#         max_length=1
#     )
#     band = models.ForeignKey("Band")


# class BandContactForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField()
#     sender = forms.EmailField()
#     cc_myself = forms.BooleanField(required=False)
