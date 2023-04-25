from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from .models import Employee


def index(request):
	employee_list = Employee.objects.order_by('FirstName')[:5]
	output = '\r\n'.join([t.FirstName for t in employee_list])
	return HttpResponse(output)

@api_view(['GET', 'POST'])
#def hello_world(request):
#    if request.method == 'POST':
#        return Response({"message": "Got some data!", "data": request.data})
#    return Response({"message": "Hello, world!"})

def ReturnData(request):
	if request.method == 'POST':
		ID = request.data['employeeId']
		match = Employee.objects.filter(EmployeeID=ID)
		if match.count() == 1:
			match = Employee.objects.get(EmployeeID=ID)
			matchname = match.FirstName + ' ' + match.LastName
			counter = 0
			if match.FirstName == request.data['firstName']:
				counter += 10000
			if match.LastName == request.data['lastName']:
				counter += 1000
			if match.EmployeePhoneNum == request.data['employeePhoneNumber']:
				counter += 100
			if match.EmployeeEmail == request.data['employeeEmail']:
				counter += 10
			if str(match.OfficeID) == request.data['officeId']:
				counter += 1
			if counter == 11111:
				matchfinal = "The information is valid for the employee " + matchname
			if counter != 11111:
				matchfinal = "The entered information is not valid, please try again. Error: " + str(counter)
			return Response(matchfinal)
		else:
			return Response("There is more than one employee with the given ID")
	return Response({"message": "That was the first name."})

