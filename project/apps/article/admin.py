from django.contrib import admin

from models import Article
    
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'is_active', 'in_list', 'date_start',)
    list_filter = ('date_start', 'is_active', )
    
admin.site.register(Article, ArticleAdmin)