from django.urls import path
from . import views

urlpatterns = [
    path('api/add', views.api_add, name='api_add'),
    path('api/update', views.api_update, name='api_update'),
    path('api/delete', views.api_delete, name='api_delete'),
    path('api/get_list', views.api_get_list, name='api_get_list'),
    path('monitor/add', views.monitor_add, name='monitor_add'),
    path('monitor/update', views.monitor_update, name='monitor_update'),
    path('monitor/delete', views.monitor_delete, name='monitor_delete'),
    path('monitor/get_list', views.monitor_get_list, name='monitor_get_list'),
]
