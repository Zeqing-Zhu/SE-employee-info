from django.db import models
from django.core.validators import RegexValidator

class Employee(models.Model):
	objects = models.Manager()
	FirstName = models.CharField(max_length=50)
	LastName = models.CharField(max_length=50)
	EmployeeID = models.IntegerField(unique=True)
	EmployeePhoneNum = models.CharField(max_length=12, unique=True, validators=[RegexValidator(regex='^.{11}$', message='Include Country Code', code='nomatch')])
	isVerified = models.BooleanField(blank=False, default=False)
	counter = models.IntegerField(default=0, blank=False)
	EmployeeEmail = models.CharField(max_length=50, unique=True)
	OfficeID = models.IntegerField(default=1)	
	AddedDate = models.DateTimeField('date added')

	def __str__(self):
		return self.FirstName

	def EmployeeName(self):
		Name = self.FirstName + ' ' + self.LastName
		return Name

	def ValidPhoneNum(self):
		PhoneNum = str(self.EmployeePhoneNum)
		return len(PhoneNum) == 11
