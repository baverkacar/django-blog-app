from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):

    # We binding auth.user with it's foreign key.
    #  on_Delete parameteres deletes everything about article when delete it on it's id.
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE)
    title = models.CharField(max_length=50)
    content = RichTextField()
    created_date = models.DateTimeField(auto_now=True)
    article_image = models.FileField(blank = True, null = True, verbose_name="Add image to article")
    
    def __str__(self):
        return self.title # This shows article title on panel.
    class Meta:
        ordering = ['-created_date']
        
class Comment(models.Model):

    # we binding Article with it's foreign key.
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Makale",related_name="comments")
    comment_author = models.CharField(max_length = 50,verbose_name = "İsim")
    comment_content = models.CharField(max_length = 200,verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content # This shows comment title on panel.
    class Meta:
        ordering = ['-comment_date']
