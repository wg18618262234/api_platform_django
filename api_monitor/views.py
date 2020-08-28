from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET, require_POST
from .models import API, Monitor, RequestLog
import logging
import json
# Create your views here.
logger = logging.getLogger('log')


@require_POST
def api_add(request):
    data_dict = json.loads(request.body)
    API.objects.create(**data_dict)
    return JsonResponse({"code": "1"})


@require_POST
def api_update(request):
    data_dict = json.loads(request.body)
    API.objects.filter(id=data_dict.pop('id')).update(**data_dict)
    return JsonResponse({"code": "1"})


@require_POST
def api_delete(request):
    data_dict = json.loads(request.body)
    API.objects.filter(id=data_dict.get('id')).delete()
    return JsonResponse({"code": "1"})


@require_GET
def api_get_list(request):
    api = API.objects.all()
    result = []
    for i in api:
        result.append(i.to_dict())
    return JsonResponse({'result': result})


@require_POST
def monitor_add(request):
    data_dict = json.loads(request.body)
    api_id = data_dict.pop('api_id')
    apis = API.objects.filter(id__in=api_id)
    monitor = Monitor.objects.create(**data_dict)
    monitor.api.add(*apis)
    return JsonResponse({"code": "1"})


@require_POST
def monitor_update(request):
    data_dict = json.loads(request.body)
    monitor = Monitor.objects.get(id=data_dict.pop('id'))
    api_id = data_dict.pop('api_id')
    apis = API.objects.filter(id__in=api_id)
    monitor.api.set(apis)
    monitor.save()
    return JsonResponse({"code": "1"})


@require_POST
def monitor_delete(request):
    data_dict = json.loads(request.body)
    Monitor.objects.get(id=data_dict.get('id')).delete()
    return JsonResponse({"code": "1"})


@require_GET
def monitor_get_list(request):
    from api_monitor import tasks

    tasks.monitor.delay(4)
    monitor = Monitor.objects.all()
    result = []
    for i in monitor:
        api = []
        for j in i.api.all():
            api.append(j.to_dict())
        data = i.to_dict().copy()
        data['api_list'] = api.copy()
        result.append(data)
    return JsonResponse({"result": result})
    # return JsonResponse({"result": 'result'})
