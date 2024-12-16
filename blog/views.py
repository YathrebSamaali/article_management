from django.shortcuts import render, get_object_or_404, redirect
from .models import Article

# Liste des articles
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {'articles': articles})

# Créer un nouvel article
def article_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Article.objects.create(title=title, content=content)
        return redirect('article_list')
    return render(request, 'blog/article_create.html')

# Modifier un article existant
def article_update(request, id):
    article = get_object_or_404(Article, pk=id)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('article_list')
    return render(request, 'blog/article_update.html', {'article': article})

# Supprimer un article
def article_delete(request, id):
    article = get_object_or_404(Article, pk=id)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'blog/article_delete.html', {'article': article})
