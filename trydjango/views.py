import random
from django.http import HttpResponse


def home_view(request):
    """
    Take in a request (Dango sends request)
    Return HTML as a response (We pick to return the response)
    """
    name = "Vadim"
    number = random.randint(10,123123123) # Can be some API call to REST API...

    # Django templates
    H1_STRING = f"""
    <h1>Hello {name} - {number}!</h1>
    """

    P_STRING = f"""
    <p>Hello {name} - {number}!</p>
    """
    HTML_STRING = H1_STRING + P_STRING
    return HttpResponse(HTML_STRING)