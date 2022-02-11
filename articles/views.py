from django.shortcuts import render, get_object_or_404
from articles.models import Article

# Create your views here.

def article_search_view(request):
    # print(dir(request))
    # print(request.GET)
    query_dict = request.GET # this is a dictionary
    try:
        query = int(query_dict.get('q'))
    except:
        query = None
    article_obj = None
    if query is not None:
    # article_obj = get_object_or_404(Article, id=query)
        article_obj = Article.objects.get(id=query)


    context = {
        "object": article_obj
    }

    return render(request, 'articles/search.html', context=context)

def detail_view(request, id=None):
    article_obj = get_object_or_404(Article, id=id)
    context = {
        "article_obj": article_obj
    }

    return render(request, 'articles/detail.html', context=context)
