from django.db import models
from datetime import date
from django.utils import timezone


class CustomerInfo(models.Model):
	class Meta:
		verbose_name_plural = 'CustomerInfo'
	customerID = models.EmailField(unique=True,null=False)
	street = models.CharField(max_length=50, blank=True,null=True)
	city = models.CharField(max_length=25, blank=True,null=True)
	state = models.CharField(max_length=20, blank=True,null=True)
	def __unicode__(self):
		return self.customerID

class RelationInfo(models.Model):
	class Meta:
		verbose_name_plural = 'RelationInfo'
	deviceID = models.IntegerField(unique=True,null=False)
	customer = models.ForeignKey(CustomerInfo,null=True)
	def __unicode__(self):
		return str(self.deviceID)

class DeviceBook(models.Model):
	class Meta:
		verbose_name_plural = 'DeviceBook'
	address = models.CharField(max_length=15)	
	status = models.BooleanField(default=False)##true is active##
	value = models.CharField(max_length=10)##TEMP,HUM,CO1,MO## 
	def __unicode__(self):
		return self.address	

class TempInfo(models.Model):
	class Meta:
		verbose_name_plural = 'TempInfo'
	device = models.ForeignKey(RelationInfo,null=True)
	temperature = models.DecimalField(max_digits=5,decimal_places=2)
	time = models.DateTimeField(default=timezone.now())
	user = models.ForeignKey(DeviceBook,null=True)
	

class HumInfo(models.Model):
	class Meta:
		verbose_name_plural = 'HumInfo'
	device = models.ForeignKey(RelationInfo,null=True)
	humidity = models.IntegerField(null=True)
	time = models.DateTimeField(default=timezone.now())
	

class CO1Info(models.Model):
	class Meta:
		verbose_name_plural = 'CO1Info'
	device = models.ForeignKey(RelationInfo,null=True)
	CO1 = models.IntegerField(null=True)
	time = models.DateTimeField(default=timezone.now())

class MoInfo(models.Model):
	class Meta:
		verbose_name_plural = 'MotionInfo'
	device = models.ForeignKey(RelationInfo,null=True)
	motion = models.BooleanField(default=False)
	time = models.DateTimeField(default=timezone.now())
	user = models.ForeignKey(DeviceBook,null=True)

	

