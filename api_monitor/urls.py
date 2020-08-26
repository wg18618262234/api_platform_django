from django.urls import path
from . import views

urlpatterns = [
    path('api/add', views.api_add, name='api_add')
]
