# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Category, Article
from .forms import ArticleForm


def index(request):
    article_list = Article.objects.all()
    category_list = Category.objects.all()

    context = {'article_list': article_list, 'category_list': category_list}
    return render(request, 'index.html', context)


def category_article(request, category_id=''):
    articles = Article.objects.filter(category=category_id)
    category_list = Category.objects.all()
    context = {'articles': articles, 'category_list': category_list}
    return render(request, 'category_article.html', context)


def article(request, article_id=''):
    article = Article.objects.get(id=article_id)
    category_list = Category.objects.all()
    context = {'article': article, 'category_list': category_list}
    return render(request, 'article.html', context)


def add_article(request, id=''):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            category = form.cleaned_data['category']
            article = Article(title=title, content=content, category=category)
            article.save()
        context = {'article': article}
        return redirect('/')
        return render(request, 'add_article.html', context)
    else:
        form = ArticleForm()
        context = {'form': form}
        return render(request, 'add_article.html', context)
