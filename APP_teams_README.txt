Notes for accessing and interacting with the Employee Info Server:

6 Different Actions. 1-2 uses HTTP Post. 3-5 use HTTP Get. 6 uses browser and UI

<str:id> is the Employee ID Number

1. Checking Information is correct:
	Endpoint: http://54.158.192.252/employee/table/
	HTTP Post sample:

{
    "firstName": "Brian",
    "lastName": "Thomas",
    "employeeId": "2",
    "employeePhoneNumber": "16157391882",
    "employeeEmail": "brianwthomas2@gmail.com",
    "officeId": "1"
}

2. Verifying OTP
	Endpoint: http://54.158.192.252/employee/OTP/<str:id>/
	HTTP Post sample:
{
    "OTP": "XXXXXX"
}
	Note: The final " / " of the endpoint is required

3. Verifying Email Account:
	Endpoint: http://54.158.192.252/employee/email_service/v_email/<str:id>
	HTTP Get Request
	Note: SLU emails do not work. Gmail accounts do work. Others will probably work

4. Sending Email with OTP:
	Endpoint: http://54.158.192.252/employee/email_service/email/<str:id>
	HTTP Get Request
	Note: SLU emails do not work. Gmail accounts do work. Others will probably work


5. Sending SMS with OTP:
	Endpoint: http://54.158.192.252/employee/email_service/sms/<str:id>
	HTTP Get Request

Notes: For 2-4 by using the employee ID as the <id> in the endpoint, 
the system will check for the required phone number/email address for the 
given employee and send the requested information.


6. Admin portal to add/alter/delete employee information
	Endpoint: http://54.158.192.252/employee/admin/table/employee/
	Notes: if you would like to add yourself for testing purposes we can add
	team members as employees in the server
