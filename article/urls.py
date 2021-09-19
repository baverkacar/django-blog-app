from django.contrib import admin
from django.urls import path
from . import views

# Create article app name for take urls later from this file.
app_name = "article"

urlpatterns = [
    path("", views.articles, name ="articles"),
    path("dashboard",  views.dashboard, name = "dashboard"),
    path("addArticle",  views.addArticle, name = "addArticle"),
    path("article/<int:id>", views.detail, name ="detail"),
    path("update/<int:id>", views.updateArticle, name ="update"),
    path("delete/<int:id>", views.deleteArticle, name ="delete"),
    path("comment/<int:id>", views.addComment, name ="comment"),

]