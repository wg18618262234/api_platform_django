from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

def api_add(request):
    return JsonResponse({"hello":"worlds"})