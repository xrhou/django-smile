# !/usr/bin/python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render

from books.models import Book


# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})


def search_form(request):
    return render(request, 'books/search_form.html')


def search(request):
    errors = []
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if q is None or q == "":
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'books/search_result.html', {'books': books, 'query': q})
    else:
        return render(request, 'books/search_form.html', {'errors': errors})


def contact_form(request):
    return render(request, 'books/contact_form.html')


def contact(request):
    errors = []
    if request.method == 'POST':
        if request.POST['subject'] is None or request.POST['subject'] == "":
            errors.append('Enter a subject.')
        if request.POST['message'] is None or request.POST['message'] == "":
            errors.append('Enter a message.')
        if request.POST['email'] is None or request.POST['email'] == "":
            errors.append('Enter a valid e-mail address.')
        if not errors:
            subject = request.POST['subject']
            email = request.POST.get('email', 'noreply@example.com')
            message = request.POST['message']
            print "subject:" + subject + ",email:" + email + ",message:" + message
            # return HttpResponseRedirect('books/thanks/')
    return render(request, 'books/contact_form.html', {'errors': errors})
