from django.conf.urls.defaults import *

urlpatterns = patterns('article.views',
   url(r'^$', 'index', name='article'),
   url(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/$', 'show', name='article_show'),
)
