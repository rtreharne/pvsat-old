from django.shortcuts import render
from blog.models import Article

def articles(request):
    articles = Article.objects.order_by('-pub_date')
    return render(request, 'articles.html', {'articles': articles})


