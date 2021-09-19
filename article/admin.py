from django.contrib import admin
from .models import Article,Comment

admin.site.register(Comment)

@admin.register(Article) # Customizing admin panel with this decorator function 
class ArticleAdmin(admin.ModelAdmin):
    
    # Displaying articles on admin panel
    
    list_display = ["title", "author", "created_date"] 
    list_display_links = ["title", "author"] 
    search_fields = ["title"]
    list_filter = ["created_date"]
    class Meta:
        model = Article
        # This Meta class is a class given to us by django. Customizes according to the Article model
        # This is a constant.
