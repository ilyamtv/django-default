from django.db import models

class ArticleManager(models.Manager):
    
    def list_query(self):
        q = self.filter(is_active=1, in_list=1)
        return q
    
    def get_active(self):
        q = self.filter(is_active=1)
        return q