from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from rest_auth.registration.serializers import RegisterSerializer



class UserSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = get_user_model()
		fields = ['id','username','email','firstname','lastname','phone','image','role']



class CustomRegisterSerializer(RegisterSerializer):
	firstname = serializers.CharField()
	lastname  = serializers.CharField()
	phone     = serializers.CharField()
	image     = serializers.ImageField()
	role      = serializers.ChoiceField(choices=User.ROLE_CHOICES)


	def get_cleaned_data(self):
		data_dict = super().get_cleaned_data()
		data_dict['firstname'] = self.validated_data.get('firstname', '')
		data_dict['lastname'] = self.validated_data.get('lastname', '')
		data_dict['phone'] = self.validated_data.get('phone', '')
		data_dict['image'] = self.validated_data.get('image', '')
		data_dict['role'] = self.validated_data.get('role', '')

		return data_dict

