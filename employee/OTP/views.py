from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from table.models import Employee
import pyotp
import base64


# Create your views here.
# This class returns the string needed to generate the key
class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now())) + "Some Random Secret Key"


class getEmployeePhoneNumRegistered(APIView):
    # Get an OTP & Verify the user

    @staticmethod
    def get(request, id):
        try:
            emp = Employee.objects.get(EmployeeID = id)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  # False Call

        phone = emp.EmployeePhoneNum
        day = datetime.now()
        daily = day.hour + day.day
        emp.counter = 1  # Update Counter At every Call
        emp.save()  # Save the data
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
        OTP = pyotp.HOTP(key)  # HOTP Model for OTP is created
        Pass = str(OTP.at(daily))
        # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
        return Response({"OTP": "EnterOTP"}, status=200)  # Just for demonstration


# Verifying the OTP
    @staticmethod
    def post(request, id):
        day = datetime.now()
        daily = day.hour + day.day
        emp = Employee.objects.get(EmployeeID = id)
        phone = emp.EmployeePhoneNum
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())
        OTP = pyotp.HOTP(key)
        if OTP.verify(request.data["OTP"], daily):
            emp.isVerified = True
            emp.save()
            return Response("OTP verification succeeded", status=200)
        return Response("OTP is wrong", status=400)
