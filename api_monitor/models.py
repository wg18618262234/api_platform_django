from django.db import models

# Create your models here.


class API(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    method = models.CharField(max_length=200)
    query = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Monitor(models.Model):
    api = models.ManyToManyField(API)
    name = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class RequestLog(models.Model):
    status_code = models.BigIntegerField()
    api_id = models.ForeignKey(API, on_delete=models.CASCADE)
    request = models.JSONField()
    response = models.JSONField()
    time_line = models.TimeField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return
