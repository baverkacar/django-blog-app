from django import forms
from .models import Article

# Create the form class.
class ArticleForm(forms.ModelForm):
     class Meta:
        model = Article
        fields = ['title', 'content','article_image']