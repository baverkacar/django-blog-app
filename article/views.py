from article.forms import ArticleForm
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404,reverse
from .models import Article, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request): 
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        if len(articles) == 0:
            messages.warning(request, "There is no article that you have been searched")
        return render(request,"articles.html",{"articles":articles})
    articles = Article.objects.all()
    return render(request,"articles.html",{"articles":articles})


@login_required 
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles": articles
    }
    return render(request, "dashboard.html", context)


@login_required
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False) # Since the author is not clear, we told it not to commit without specifying the author.
        article.author = request.user
        article.save()

        messages.success(request, "Article added successfully")
        return redirect("article:dashboard")

    return render(request, "addArticle.html",{"form":form})


def detail(request, id):

    # article = Article.objects.filter(id = id).first() is list so ı take the first element of it.
    article = get_object_or_404(Article, id = id)
    comments = article.comments.all()
    return render(request,"detail.html",{"article":article,"comments":comments})


@login_required
def updateArticle(request, id):

    article = get_object_or_404(Article, id = id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance = article)
    if form.is_valid():
        article = form.save(commit=False) # Since the author is not clear, we told it not to commit without specifying the author.
        article.author = request.user
        article.save()
        messages.success(request, "Article updated successfully")
        return redirect("article:dashboard")
    return render(request, "update.html", {"form": form})


@login_required
def deleteArticle(request, id):
    article = get_object_or_404(Article, id = id)
    article.delete()
    messages.success(request, "Article deleted successfully")
    return redirect("article:dashboard")


def addComment(request, id):
    article = get_object_or_404(Article,id = id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_author  = comment_author, comment_content = comment_content)
        newComment.article = article
        newComment.save()

    return redirect(reverse("article:detail",kwargs={"id":id})) # For dynamic url we need to reverse it.