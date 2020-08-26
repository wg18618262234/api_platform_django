from django.db import models

# Create your models here.


class API(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    method = models.CharField(max_length=200)
    query = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    create_time = models.DateTimeField('create_time')
    update_time = models.DateTimeField('update_time')


class Monitor(models.Model):
    api = models.ForeignKey(API, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    api_ids = models.CharField(max_length=200)
    create_time = models.DateTimeField('create_time')
    update_time = models.DateTimeField('update_time')
