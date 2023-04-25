from django.shortcuts import render
from django.core.mail import send_mail
from datetime import datetime
from OTP.views import generateKey
from table.models import Employee
import boto3
import pyotp
import base64

#Verify Email by id
def verifyemail(request, id):
    if request.method == 'GET':
        ID = Employee.objects.get(EmployeeID = id)
        email = str(ID.EmployeeEmail)

        ses = boto3.client('ses',
                           aws_access_key_id="token",
                           aws_secret_access_key="token",
                           region_name="us-east-1"
                           )

        ses.verify_email_identity(EmailAddress = email)

    return render(request, 'email_service/verify.html')

# Create your views here.
def sendemail(request,id):
    emp = Employee.objects.get(EmployeeID = id)
    phone = emp.EmployeePhoneNum
    keygen = generateKey()
    key = base64.b32encode(keygen.returnValue(phone).encode())
    OTP = pyotp.HOTP(key)
    day = datetime.now()
    daily = day.hour + day.day
    OTP = OTP.at(daily)
    
    Subject = "Sign in Verification for CSCI 5300 Project"
    Message = "Your One-Time-Password is: " + str(OTP)
    send_mail(
        Subject,
        Message,
        'kitchana.thamutok@slu.edu',
        [emp.EmployeeEmail],
        fail_silently=False,
    )
    return render(request,'email_service/index.html')

def sendsms(request, id):
    if request.method == 'GET':
        emp = Employee.objects.get(EmployeeID = id)
        phoneNumber = emp.EmployeePhoneNum

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phoneNumber).encode())
        OTP = pyotp.HOTP(key)
        day = datetime.now()
        daily = day.hour + day.day
        OTP = OTP.at(daily)

        # Create an SNS client
        client = boto3.client(
            "sns",
            aws_access_key_id="token",
            aws_secret_access_key="token",
            region_name="eu-west-1"
        )

        # Send your sms message.
        client.publish(
            PhoneNumber=phoneNumber,
            Message = "Your One-Time-Password is: " + OTP
        )
        return render(request,'email_service/index.html')
