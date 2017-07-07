from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<category_id>[\w]+)$',
        views.category_article, name='category'),
    url(r'^article/(?P<article_id>[\d]+)$', views.article, name='article'),
    url(r'^addarticle$', views.add_article, name='add'),
]
