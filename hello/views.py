from django.shortcuts import render
from django.http import HttpResponse # for the http response rendering at the browser.

# Create your views here.
# view to show the hello world statement.
def hello_world(request):
    return HttpResponse('Hello world!')

