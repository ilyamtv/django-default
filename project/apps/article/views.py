from django.shortcuts import get_object_or_404, render_to_response
from django.http import Http404
from annoying.decorators import *

from models import Article

@render_to('article/index.html')
def index(request):
    articles = Article.objects.list_query()
    
    return { 'articles': articles }

@render_to('article/show.html')
def show(request, id, slug):
    try:
        article = Article.objects.get_active().get(pk=id, slug=slug)
    except:
        raise Http404
    
    return { 'article': article }
