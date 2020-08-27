from django.db import models

# Create your models here.


class API(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    method = models.CharField(max_length=200)
    params = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url,
            'method': self.method,
            'params': self.params,
            'body': self.body,
            'create_time': self.create_time,
            'update_time': self.update_time,
        }


class Monitor(models.Model):
    api = models.ManyToManyField(API)
    name = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'create_time': self.create_time,
            'update_time': self.update_time,
        }


class RequestLog(models.Model):
    status_code = models.BigIntegerField()
    api_id = models.ForeignKey(API, on_delete=models.CASCADE)
    request = models.JSONField()
    response = models.JSONField()
    time_line = models.TimeField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.api_id

    def to_dict(self):
        return {
            'id': self.id,
            'api_id': self.api_id,
            'status_code': self.status_code,
            'request': self.request,
            'response': self.response,
            'create_time': self.create_time,
            'update_time': self.update_time,
        }
