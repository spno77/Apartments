from django.db import models

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image

from django.utils.translation import ugettext_lazy as _
	
class UserManager(BaseUserManager):
	def create_user(self, username, email, password=None):
		if username is None:
			raise TypeError('Users must have a username.')
		if email is None:
			raise TypeError('Users must have an email address.')

		user = self.model(username=username, email=self.normalize_email(email))
		user.set_password(password)
		user.save()

		return user

	def create_superuser(self, username, email, password):

		if password is None:
			raise TypeError('Superusers must have a password.')
		user = self.create_user(username, email, password)
		user.is_superuser = True
		user.is_staff = True
		user.save()

		return user


class User(AbstractBaseUser, PermissionsMixin):
	
	GUEST = 'guest'
	HOST = 'host'
	COSTUMER = 'costumer'

	ROLE_CHOICES = [
		(GUEST,_('guest')),
		(HOST,_('host')),
		(COSTUMER,_('costumer')),
	]	

	
	username = models.CharField(db_index=True, max_length=255, unique=True,null=False)
	email = models.EmailField(db_index=True, unique=True,null=False)
	is_staff = models.BooleanField(default=False)
	firstname = models.CharField(max_length=30,null=False)
	lastname = models.CharField(max_length=30,null=False)
	phone = models.CharField(max_length=12,null=False)
	image = models.ImageField(default='default.jpg',upload_to='images')
	role = models.CharField(max_length=10,choices=ROLE_CHOICES,default=GUEST)
	
	
	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']


	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)


	def __str__(self):
		return self.username



	