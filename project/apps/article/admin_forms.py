from django import forms

from models import Article
from core.ckeditor import CKEditor

class ArticleAdminForm(forms.ModelForm):
    
    class Meta:
        model = Article
        widgets = {
            'title': forms.TextInput(attrs={'size': 100}),
            'slug': forms.TextInput(attrs={'size': 100}),
            'content': CKEditor(),
            'short_content': forms.Textarea(attrs={'rows': 5, 'cols': 80}),
        }