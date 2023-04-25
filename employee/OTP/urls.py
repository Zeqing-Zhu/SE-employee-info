from django.urls import path
from .views import getEmployeePhoneNumRegistered


urlpatterns = [
	path("<str:id>/", getEmployeePhoneNumRegistered.as_view(), name="OTP Gen"),
]
