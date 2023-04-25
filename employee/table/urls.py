from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from . import views


urlpatterns = [
	path('', views.ReturnData, name='Return_Data'),
	path('employee-info/', include('rest_framework.urls', namespace='rest_framework'))
]
