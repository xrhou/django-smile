#!/usr/bin/python
# -*- coding:utf-8 -*-


from django.contrib import admin

from .models import Publisher, Author, Book, Borrower


# 作者管理
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mobile', 'email')
    search_fields = ('first_name', 'last_name')  # 查询作者


# 出版社管理显示
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'country', 'state_province', 'city', 'website')
    # search_fields = ('name')  # 查询书名


# 书管理显示
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'bookNo', 'publisher', 'publication_date')
    # list_display = ('title', 'bookNo', 'publisher', 'publication_date', 'borrower_start_date', 'borrower_end_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    # fields = ('title', 'authors', 'publisher', 'publication_date')  # 'publication_date' 被隐藏，以防编辑
    filter_horizontal = ("authors",)
    raw_id_fields = ('publisher',)


# 借书者管理
class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mobile', 'email')
    search_fields = ('first_name', 'last_name')  # 查询借书者


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Borrower, BorrowerAdmin)
