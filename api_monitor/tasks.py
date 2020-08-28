from __future__ import absolute_import
from celery import shared_task
import requests
import json
from .models import API
from celery.utils.log import get_task_logger
import logging


@shared_task
def add(x: int, y: int) -> int:
    return x+y


@shared_task
def monitor(*api_id):
    api = API.objects.filter(id__in=api_id)
    data = []
    for i in api:
        req_data = i.to_dict()
        try:
            response = requests.request(
                method=req_data.get('method'),
                url=req_data.get('url'),
                params=req_data.get('params'),
                data=req_data.get('data'),
                headers=req_data.get('headers')
            )
            logging.info(response.text)
            data.append({
                "request": {
                    "method": req_data.get('method'),
                    "url": req_data.get('url'),
                    "params": req_data.get('params'),
                    "body": req_data.get('data'),
                },
                "response": {
                    "status_code": response.status_code,
                    "response_text": response.text,
                }
            })
        except Exception as e:
            logging.error(e)
    return {
        'result': data
    }
