from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def api_add(request):
    return HttpResponse("hello world")