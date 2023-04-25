from django.urls import path, include
from . import views

urlpatterns = [
	path('email/<str:id>', views.sendemail),
	path('v_email/<id>', views.verifyemail),
	path('sms/<str:id>', views.sendsms),
]
