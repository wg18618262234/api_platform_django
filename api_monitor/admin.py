from django.contrib import admin
from .models import API, Monitor, RequestLog
# Register your models here.

admin.site.register([API, Monitor, RequestLog])
