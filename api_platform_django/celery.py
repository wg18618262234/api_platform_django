# _*_ coding:utf-8 _*_
"""
异步
创建celery实例
"""

from __future__ import absolute_import
from __future__ import unicode_literals
import os
from celery import Celery, platforms
from django.utils import timezone
from kombu import Exchange
from kombu import Queue
import datetime

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_platform_django.settings')

app = Celery("celery_app")
# app.now=datetime.datetime.utcnow
# print app.now(), 'celery---------------->>>>>>'

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# 在django配置文件中进行配置,以大写CELERY开头
app.config_from_object('django.conf:settings', namespace='CELERY')
# 解决时区问题,定时任务启动就循环输出
app.now = timezone.now
# app.now = datetime.datetime.now

# Load task modules from all registered Django app configs.
# celery自动发现所有django-app下面的任务tasks.py
app.autodiscover_tasks()

# 允许root 用户运行celery
platforms.C_FORCE_ROOT = True

# 通过设置x-max-priority参数来配置队列以支持优先级
# app.conf.task_queues = [
#     Queue('tasks', Exchange('tasks'), routing_key='tasks',
#           queue_arguments={'x-max-priority': 10}),
# ]
# 设置所有队列的默认值
# app.conf.task_queue_max_priority = 10

# 设置了三个Queue绑定到一个direct类型的exchange上,然后consumer监听所有的队列,消息来了后就轮询调用consumer进行处理.
task_exchange = Exchange('tasks', type='direct')
# 异步任务优先级
task_queues = [Queue('hipri', task_exchange, routing_key='hipri'),
               Queue('midpri', task_exchange, routing_key='midpri'),
               Queue('lopri', task_exchange, routing_key='lopri')]


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
