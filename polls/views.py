from django.shortcuts import render
from django.http import HttpResponse

# Create polls views here.
def index(request):
    return HttpResponse("Hello,World,You're at the polls index.")