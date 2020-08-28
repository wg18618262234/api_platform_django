from __future__ import absolute_import
from celery import shared_task
import requests
import logging
import json

logger = logging.getLogger('log')


@shared_task
def add(x: int, y: int) -> int:
    return x+y


@shared_task
def request(method: str, url: str, headers: dict = None, params: dict = None, data: dict = None) -> dict:
    logging.info('url:'+str(url))
    response = requests.request(
        method=method,
        url=url,
        params=params,
        data=data,
        headers=headers
    )
    return {
        "request": {
            "method": method,
            "url": url,
            "body": data
        },
        "response": {
            "status_code": response.status_code,
            "response_text": response.text
        }
    }
