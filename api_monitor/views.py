from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.


def api_add(request):
    return JsonResponse({"hello": "worlds"})


def api_update(request):
    return JsonResponse({"hello": "worlds"})


def api_delete(request):
    return JsonResponse({"hello": "worlds"})


def api_get_list(request):
    return JsonResponse({"hello": "worlds"})


def monitor_add(request):
    return JsonResponse({"hello": "worlds"})


def monitor_update(request):
    return JsonResponse({"hello": "worlds"})


def monitor_delete(request):
    return JsonResponse({"hello": "worlds"})


def monitor_get_list(request):
    return JsonResponse({"hello": "worlds"})
