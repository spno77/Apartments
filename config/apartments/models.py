from django.db import models
from django.contrib.auth import get_user_model


class Apartment(models.Model):

	description = models.CharField(max_length=50)
	price = models.FloatField()
	garage = models.BooleanField(default=False)
	wifi = models.BooleanField(default=False)
	rooms = models.IntegerField()

	owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='owner')

	def __str__(self):
		return self.description


class Availability(models.Model):

	from_date = models.DateField()
	to_date = models.DateField()

	apartment = models.ForeignKey(Apartment,on_delete=models.CASCADE,related_name='availability')

	def __str__(self):
		return f"from { str(self.from_date) } to {str(self.to_date)}"
