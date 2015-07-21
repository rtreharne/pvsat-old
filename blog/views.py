from django.shortcuts import render
from blog.models import Article

def articles(request):
    articles = Article.objects.order_by('-pub_date')
    return render(request, 'articles.html', {'articles': articles})

def article(request, article_id=1):
	article= Article.objects.get(id=article_id)
	return render(request, 'article.html', {'article': article})
	


