from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greetings(request):
    return HttpResponse("<h1> Hello friends Good Morning ... Have a Niceday</h1>")