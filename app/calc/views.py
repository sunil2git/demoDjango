from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    """this for basic test so we are passing it from response . Just a message  """
    #return HttpResponse("hello world")\
    return render(request, 'home.html', {'name':'Sunil'})
