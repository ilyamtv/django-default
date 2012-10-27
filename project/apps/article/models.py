from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _

from managers import ArticleManager

    
class Article(models.Model):
    
    class Meta:
        db_table = 'article'
        verbose_name=_('Article')
        verbose_name_plural = _('Articles')
        ordering = ['-date_start']
        
    objects = ArticleManager()
    
    title = models.CharField(null=False, blank=False, max_length=255, verbose_name=_('Title'))
    slug = models.SlugField(verbose_name=_('Slug'), max_length=255,)
    short_content = models.TextField(null=True, blank=False, verbose_name=_('Short content'))
    content = models.TextField(null=True, blank=False, verbose_name=_('Content'))
    
    date_start = models.DateTimeField(null=False, default=datetime.today(), verbose_name=_('Date start'))
    
    in_list = models.BooleanField(null=False, default=True, verbose_name=_('In list'))
    is_active = models.BooleanField(null=False, default=True, verbose_name=_('Is active'))
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('article.views.show', [self.pk, self.slug])
    