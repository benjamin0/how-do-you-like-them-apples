from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

from .models import Caller, Question, Choice


class ChoiceAdmin(admin.TabularInline):
    model = Choice
    extra = 1
    formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows': 6, 'cols': 60})},
    }


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = (ChoiceAdmin,)
    formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows': 6, 'cols': 60})},
    }
    list_display = ('question_text', 'num')


class CallerAdmin(admin.ModelAdmin):
    model = Caller
    list_display = ('name', 'phone_number', 'start_num', 'end_num', 'question_num', 'start_fresh')
    formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows': 6, 'cols': 60})},
    }

admin.site.register(Caller, CallerAdmin)
admin.site.register(Question, QuestionAdmin)