import imp
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article


def home_view(request):
    """
    Take in a request (Dango sends request)
    Return HTML as a response (We pick to return the response)
    """
    rand_id = random.randint(1,4) # Can be some API call to REST API...
    article_obj = Article.objects.get(id=rand_id)
    test_list = [100, 101, 102, 103, 104]

    # Create dictionary
    context = {
        "test_list": test_list,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }

    # Django templates
    html_response = render_to_string("home-view.html", context=context)
    return HttpResponse(html_response)