import random
from django.http import HttpResponse


def home_view(request):
    """
    Take in a request (Dango sends request)
    Return HTML as a response (We pick to return the response)
    """
    name = "Vadim"
    name2 = "Alona"
    number = random.randint(10,123123123) # Can be some API call to REST API...

    # from database?
    # article_name = ?
    # article_content = ?

    # Django templates
    H1_STRING = f"""
    <h1>Hello {name} - {number}!</h1>
    """

    P_STRING = f"""
    <p>Hello {name} - {number}!</p>
    <p>Hello {name2}!</p>
    <img src="https://soviet-art.ru/wp-content/uploads/2016/03/Legendary-Soviet-chocolate-Alyonka-1.jpg" style="width:200px;height:300px;">
    """
    HTML_STRING = H1_STRING + P_STRING
    return HttpResponse(HTML_STRING)