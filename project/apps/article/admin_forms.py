from django import forms

from models import Article

class ArticleAdminForm(forms.ModelForm):
    
    class Meta:
        model = Article
        widgets = {
            'title': forms.TextInput(attrs={'size': 100}),
            'slug': forms.TextInput(attrs={'size': 100}),
            'short_content': forms.Textarea(attrs={'rows': 5, 'cols': 80}),
        }