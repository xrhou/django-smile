from django.contrib import admin

from .models import Question, Choice

# Register polls models here.
admin.site.register(Question)
admin.site.register(Choice)
