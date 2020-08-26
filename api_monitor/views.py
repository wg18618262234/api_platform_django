from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET, require_POST
# Create your views here.


@require_POST
def api_add(request):
    return JsonResponse({"hello": "worlds"})


@require_POST
def api_update(request):
    return JsonResponse({"hello": "worlds"})


@require_POST
def api_delete(request):
    return JsonResponse({"hello": "worlds"})


@require_GET
def api_get_list(request):
    return JsonResponse({"hello": "worlds"})


@require_POST
def monitor_add(request):
    return JsonResponse({"hello": "worlds"})


@require_POST
def monitor_update(request):
    return JsonResponse({"hello": "worlds"})


@require_POST
def monitor_delete(request):
    return JsonResponse({"hello": "worlds"})


@require_GET
def monitor_get_list(request):
    return JsonResponse({"hello": "worlds"})
