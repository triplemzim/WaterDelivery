from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.


	
class City(models.Model):
	"""
	Description: City 
	"""
	name = models.CharField(max_length = 100)

	class Meta:
		pass

	def __str__(self):
		return self.name

class Thana(models.Model):
	"""
	Description: Thana names
	"""
	name = models.CharField(max_length = 100)

	cityID = models.ForeignKey(City)

	class Meta:
		pass	

class Profile(models.Model):
	firstName = models.CharField(max_length = 100)
	lastName = models.CharField(max_length = 100)
	mobileNumber = models.CharField(max_length = 15)
	signUpDate = models.DateField(default = datetime.date.today())
	activeUser = models.BooleanField(default = False)
	inactiveSince = models.DateField(default = datetime.date.today())
	
	thanaID = models.ForeignKey(Thana)
	address = models.CharField(max_length = 500)
	user = models.ForeignKey(User)
	


	def __str__(self):
		return self.firstName + ' ' + self.lastName


class ThirdPartyCompany(models.Model):
	"""
	Description: ThirdParty Company will be represented by TPC
	"""
	name = models.CharField(max_length = 200)
	email = models.EmailField(max_length = 200)
	mobileNumber = models.CharField(max_length = 15)
	address = models.CharField(max_length = 500)
	signUpDate = models.DateField(default = datetime.date.today())

	thana = models.ForeignKey(Thana)




	class Meta:
		pass


	def __str__(self):
		return self.name


class Device(models.Model):
	"""
	Description: Device info
	"""
	mobileNumber = models.CharField(max_length = 15)
	status = models.CharField(max_length = 300)
	issueDate = models.DateField(default = datetime.date.today())
	address = models.CharField(max_length = 500)
	lastStatusChanged = models.DateTimeField(default = datetime.datetime.now())

	thana = models.ForeignKey(Thana)
	userID = models.ForeignKey(User)

	class Meta:
		pass


	def __str__(self):
		return self.pk + ' ' + self.mobileNumber


class Message(models.Model):
	"""
	Description: Messages from user
	"""
	title = models.CharField(max_length = 100)
	body = models.CharField(max_length = 1000)
	time = models.DateTimeField(default = datetime.datetime.now())

	user = models.ForeignKey(User)


	class Meta:
		pass

	def __str__(self):
		return self.title



class DataLog(models.Model):
	deviceStatus = models.CharField(max_length = 1000)
	time = models.DateTimeField(default = datetime.datetime.now())

	deviceID = models.ForeignKey(Device)