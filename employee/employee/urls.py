"""employee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin

admin.site.site_header = 'Employee Info Administration'
admin.site.site_title = 'Employee Info Administration'

urlpatterns = [
    path('employee/admin/', admin.site.urls),
    path('employee/table/', include('table.urls')),
    path('employee/email_service/', include('email_service.urls')),
    path('employee/OTP/', include('OTP.urls')),
]
