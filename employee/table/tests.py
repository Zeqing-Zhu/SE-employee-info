from django.test import TestCase

from table.models import Employee
from table import views

class EmployeeModelTests(TestCase):
	
	def test_longPhoneNum(self):
		PhoneNum = 16157391882
		LongNum = Employee(EmployeePhoneNum = PhoneNum)
		self.assertIs(LongNum.ValidPhoneNum(),False)

	def test_shortPhoneNum(self):
		PhoneNum = 615739188
		ShortNum = Employee(EmployeePhoneNum = PhoneNum)
		self.assertIs(ShortNum.ValidPhoneNum(),False)

class EmployeeInfoTests(TestCase):
	def test_getsSuccessVerify(self):
		response = self.client.get('', follow=True)
		self.assertEqual(response.data['message'], 'That was the first name.')
	def test_PostGeneralError(self):
		response = self.client.post('', {
			"firstName": "teest",
			"lastName": "test",
			"employeeId": "1111",
			"employeePhoneNumber": "test",
			"employeeEmail": "test"
		}) # blank data dictionary
		self.assertEqual(response.data, 'There is more than one employee with the given ID')
