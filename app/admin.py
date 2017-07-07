# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category, Article


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'introductions')
    search_fields = ('category',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'category', 'pub_time')
    list_filter = ('pub_time',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
